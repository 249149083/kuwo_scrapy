# -*- coding: utf-8 -*-

# Scrapy settings for kuwo_scrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'kuwo_scrapy'

SPIDER_MODULES = ['kuwo_scrapy.spiders']
NEWSPIDER_MODULE = 'kuwo_scrapy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"

CONCURRENT_REQUESTS = 1

ITEM_PIPELINES = {
    'kuwo_scrapy.pipelines.KuwoScrapyPipeline' : 800,
}



LOG_FILE = 'spider.log'
LOG_LEVEL = 'DEBUG'
#LOG_LEVEL = 'ERROR'

MAIL_FROM = 'page_monitor@kuwo.cn'
MAIL_HOST = 'kwsmtp.kuwo.cn'
MAIL_USER = 'page_monitor@kuwo.cn'
#MAIL_USER = 'dawei.qian@kuwo.cn'
MAIL_PASS = 'kuwo123!@'

MIN_ALARM_LIMIT = 1
DOWNLOAD_TIMEOUT = 20

KUWO_SCRAPY_MYSQL_CS = 'utf8'
KUWO_SCRAPY_MYSQL_DB = 'Scrapy'
KUWO_SCRAPY_MYSQL_HOST = '172.17.60.35'
KUWO_SCRAPY_MYSQL_USER = 'nethin'
KUWO_SCRAPY_MYSQL_PASS = 'dipijvz7'


