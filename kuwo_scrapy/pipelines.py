# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import hashlib
import MySQLdb

from MySQLdb import cursors
from datetime import datetime

from scrapy import log
from scrapy.mail import MailSender
from scrapy.exceptions import *

from kuwo_scrapy.settings import *

class KuwoScrapyDBConnector(object):
    conn = None
    spider = None
    cursor = None
    cursor_type = None
    spider_inware = None
    now = None

    def init(self):
        self.connect()
        self.set_cursor()

    def reset_cursor(self):
        try:
            if self.cursor:
                log.msg("Try to reset cursor from %s" % (KUWO_SCRAPY_MYSQL_DB), log.INFO)
                self.cursor = self.conn.cursor(self.cursor_type)
        except Exception,e:
            log.msg("Reset Cursor error : %s" % (e), log.INFO)
            exit()


    def set_cursor(self, cursor_type = MySQLdb.cursors.DictCursor):
        try:
            log.msg("Try to get cursor from %s" % (KUWO_SCRAPY_MYSQL_DB))
            self.cursor = self.conn.cursor(cursor_type)
            self.cursor_type = cursor_type
        except Exception,e:
            log.msg("Get Cursor error : %s" % (e), log.ERROR)
            self.reset_cursor(self)


    def connect(self):

        try:
            log.msg("Try to connecting to %s on %s" % (KUWO_SCRAPY_MYSQL_DB, KUWO_SCRAPY_MYSQL_HOST), log.INFO)
            self.conn = MySQLdb.connect(host = KUWO_SCRAPY_MYSQL_HOST, user = KUWO_SCRAPY_MYSQL_USER, 
                                           passwd = KUWO_SCRAPY_MYSQL_PASS, db = KUWO_SCRAPY_MYSQL_DB, charset = KUWO_SCRAPY_MYSQL_CS)
        except Exception,e:
            log.msg("Connect error : %s" % (e), log.ERROR)

    def close(self):
        try:
            if self.conn and self.cursor:
                log.msg("Disconnect to %s on %s" % (KUWO_SCRAPY_MYSQL_DB, KUWO_SCRAPY_MYSQL_HOST), log.INFO)
                self.cursor.close()
                self.conn.commit()
                self.conn.close()
                self.cursor = None
                self.conn = None
            else:
                log.msg("Connection %s is disconnected" % (KUWO_SCRAPY_MYSQL_DB, KUWO_SCRAPY_MYSQL_HOST), log.INFO)

        except Exception,e:
            log.msg("Disconnect error : %s" % (e), log.ERROR)

    def __init__(self, spider):
        self.now = datetime.strftime(datetime.now(), '%Y-%m-%d %X')
        self.spider = spider
        self.init()
        self.spider_inware = self.getSpiderInware()

    def getFieldNames(self, table):
        fields = self.getFields(table)
        field_names = []
        for field in fields:
            field_names.append(field['Field'])

        return field_names


    def getFields(self, table):
        fields = {}
        try:
            self.cursor.execute('desc %s' % table)
            fields = self.cursor.fetchall()
#            log.msg('Get fields of %s: \n%s' % (table, json.dumps(fields, indent = 2)), log.DEBUG)
        except Exception,e:
            log.msg('Get fields of %s error : %s' % (table, e), log.ERROR)
        return fields

    def genSpiderInware(self):
        try:
            log.msg('Add a new spider : %s' % (self.spider.name), log.INFO)
            self.cursor.execute("insert into spider(m_name,basic_desc,m_info,c_status) values('%s','%s','%s',1)" % (self.spider.name, self.spider.desc, self.spider.info))
            self.conn.commit()
        except Exception,e:
            log.msg('Insert spider error : %s' % (e), log.ERROR)
            exit()

    def getSpiderInware(self):
        if self.spider_inware:
            return self.spider_inware

        try:
            log.msg('Fetch spider : %s' % (self.spider.name), log.INFO)
            self.cursor.execute("select * from spider where m_name = '%s'" % (self.spider.name))
            self.spider_inware = self.cursor.fetchone()
        except Exception,e:
            log.msg('Fetch spider error : %s' % (e), log.ERROR)
            
        if not self.spider_inware:
            self.genSpiderInware()
            self.spider_inware = self.getSpiderInware()

        return self.spider_inware

    def checkInsertItem(self, item):
        field_names = self.getFieldNames('crawl_music')
        crawled = False

        try:
            md5_source = "%(basic_source_name)s%(basic_source_artist)s%(basic_source_info)s" % item
            md5_source += self.spider.name
            c_unique_key = hashlib.md5(md5_source).hexdigest()

            keys = ['c_unique_key', 'm_crawl_date']
            values = [c_unique_key, self.now]
            item['m_spider_id'] = str(self.spider_inware['id'])

            for key in item:
                keys.append(key)
                values.append(item[key].replace('"','\\"'))

            sql_key = 'crawl_music(%s)' % (','.join(keys))
            sql_value = 'values("%s")' % ('","'.join(values))
            
            sql = ' '.join(['insert ignore into',sql_key,sql_value])

            log.msg("Check or insert item sql : %s" % (sql), log.DEBUG)
            crawled = self.cursor.execute(sql) > 0
        except Exception,e:
            raise DropItem("Check or insert item error : %s" % (e))

        return crawled


    def getAddrList(self):
        addr_list = []
        try:
            log.msg("Get addr list", log.INFO)
            sql = "select user.m_email from user left join alarm on alarm.m_user_id = user.id left join spider on spider.id = alarm.m_spider_id where spider.id = %d and user.c_alarm_level > 0 order by user.c_alarm_level desc" % (self.spider_inware['id'])
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            addr_list = [row['m_email'] for row in rows]
        except Exception,e:
            log.msg("Get addr list error : %s" % (e), log.ERROR)
        return addr_list


global MIN_ALARM_LIMIT
class KuwoScrapyMailWriter():
    spider = None
    num_new = 0
    new_list = []
    item_list = []
    addr_list = []
    mail_sender = None
    mail_content = ''
    spider_inware = None
    
    def __init__(self,spider , spider_inware, addr_list):
        self.mail_sender = MailSender(smtphost = MAIL_HOST, mailfrom = MAIL_FROM, smtpuser = MAIL_USER,
                                      smtppass = MAIL_PASS)
        self.spider = spider
        self.addr_list = addr_list
        self.spider_inware = spider_inware


    def push(self, item, crawled):
        if crawled:
            self.num_new += 1
        self.new_list.append(crawled)
        self.item_list.append(item)


    def write_mail(self):
        lines = []
        head = "<h1>%s</h1><hr/><ol>" % self.spider_inware['basic_desc']
        tail = "</ol><hr/>%s" % self.spider_inware['m_info']
        for item in self.item_list:
            mark = ''
            info = json.loads(item['basic_source_info'])
            info_str = '<span>' + json.dumps(info, indent = 2) + '</span>'

            if self.new_list[len(lines)]:
                mark = '########'

            line = '<li>' + mark
            if item['basic_source_artist']:
                line += '%(basic_source_artist)s - %(basic_source_name)s ' % item
            else:
                line += '%(basic_source_name)s ' % item

            if info:
                line += info_str

            line += '</li>'
            line = line.decode(KUWO_SCRAPY_MYSQL_CS)

            lines.append(line)
            
            
        html_head = '<div>'
        html_tail = '</div>'

        if self.spider.start_urls:
            index = 1
            for url in self.spider.start_urls:
                if url:
                    html_tail += u'<a href="%s" target="_blank">连接%d</a>&nbsp;' % (url, index)
                    index += 1

        self.mail_content = head + '\n'.join(lines) + tail
        log.msg("Write mail : \n %s" % self.mail_content, log.DEBUG)
        self.mail_content = html_head + self.mail_content + html_tail



    def send_mails(self):
        log.msg("Sending mail :: \n num_new : %d \n spider_inware : %s \n addr_list : %s" % (self.num_new, json.dumps(self.spider_inware, indent = 2), 
                                                                                             json.dumps(self.addr_list, indent = 2)), log.DEBUG )
        if (self.num_new < MIN_ALARM_LIMIT) or (not self.spider_inware) or (len(self.addr_list) < 1):
            return

        self.write_mail()
        try:
            addr = "<%s>" % ('>,<'.join(self.addr_list))
            log.msg("Sending mail to %s" % (addr), log.INFO)
            self.mail_sender.send(to = self.addr_list, subject = self.spider_inware['basic_desc'], 
                                  body = self.mail_content.encode('utf-8','ignore'), 
                                  mimetype = 'text/HTML;charset="utf-8"')
        except Exception,e:
            log.msg("Sendding mail error : %s" %(e), log.ERROR)
        
    

class KuwoScrapyPipeline(object):
    connector = None
    mailwritor = None
    
    def open_spider(self, spider):
        self.connector = KuwoScrapyDBConnector(spider)
        addr_list = self.connector.getAddrList()
        self.mailwritor = KuwoScrapyMailWriter(spider, self.connector.spider_inware, addr_list)

    def process_item(self, item, spider):
        for key in item:
                item[key] = item[key].encode(KUWO_SCRAPY_MYSQL_CS).strip()
        try:
            if self.connector.spider_inware['c_status'] != 0:
                raise DropItem("spider is closed!")
            crawled = self.connector.checkInsertItem(item)
            self.mailwritor.push(item, crawled)
        except Exception,e:
            self.connector.conn.rollback()
            raise DropItem("%s" % (e))

        return item

    def close_spider(self, spider):
        self.connector.close()
        self.mailwritor.send_mails()

