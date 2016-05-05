# -*- coding: utf-8 -*-
import scrapy

from kuwo_scrapy.items import KuwoScrapyItem
from kuwo_scrapy.pipelines import KuwoScrapyDBConnector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst
from scrapy.exceptions import *

class QqWebNewAlbumSpider(scrapy.Spider):
    desc = u"[QQWeb端首页]在线首发"
    info = u"qq音乐web首页>在线首发,10张专辑。"
    name = 'qq_web__new_album'
    allowed_domains = ["i.y.qq.com"]
    
    start_urls = (
        'http://y.qq.com/#type=index',
    )
    
    filter_css = '//ul[@class="mod_first_list"]/li'
    name_css = 'strong.album_name::attr(title)'
    artist_css = 'strong.album_singer::attr(title)'
    count_limit = 10
    
    def parse(self, response):
	try:
            movies = response.xpath(self.filter_css)
	    print "movies: ",movies

        except Exception,e:
            err = self.name + ':' + str(e)
            raise CloseSpider(err)


        count = 0
        for movie in movies:
            count += 1
            if count > self.count_limit:
                raise CloseSpider('done')

            loader = ItemLoader(KuwoScrapyItem(), movie)
		
            loader.add_value('basic_source_info', '{}')
            loader.add_css('basic_source_name', self.name_css, Join())
            loader.add_css('basic_source_artist', self.artist_css, Join())
            yield loader.load_item()
 
class QqWebMvSpider(QqWebNewAlbumSpider):
    desc = u"[QQMV]改变通知"
    info = u"QQ音乐首页，MV首播，标签下8个视频"
    name = 'qq_web__mv'
    allowed_domains = ["i.y.qq.com"]
    start_urls = (
        'http://y.qq.com/#type=index',
    )
    filter_css = '//ul[@class="mod_mv_list"]/li'
    name_css = 'a.mv_name::attr(title)'
    artist_css = 'a.singer_name::attr(title)'
    count_limit = 8
