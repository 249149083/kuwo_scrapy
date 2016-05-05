# -*- coding: utf-8 -*-
import scrapy

from kuwo_scrapy.items import KuwoScrapyItem
from kuwo_scrapy.pipelines import KuwoScrapyDBConnector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst
from scrapy.exceptions import *

class IqiyiWebZySpider(scrapy.Spider):
    desc = u"[爱奇艺首页]综艺"
    info = u"首页>综艺(前7)"
    name = "iqiyi_web__zy"
    allowed_domains = ["www.iqiyi.com"]
    start_urls = (
        'http://www.iqiyi.com/',
    )
    first_css = 'div#block-G div.flow-twoBlock div.site-piclist_info p.site-piclist_info_title a'
    second_css = '::attr(title)'
    count_limit = 7
    
    def parse(self, response):
        try:
            movies = response.css(self.first_css)
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
            loader.add_css('basic_source_name', self.second_css, Join())
            loader.add_value('basic_source_artist', '')
            yield loader.load_item()


class IqiyiWebMovieSpider(IqiyiWebZySpider):
    desc = u"[爱奇艺首页]电影"
    info = u"首页>电影(前10)"
    name = "iqiyi_web__movie"
    allowed_domains = ["www.iqiyi.com"]
    start_urls = (
        'http://www.iqiyi.com/',
    )
    first_css = 'div#block-L div.site-main-outer div.site-piclist_info p.site-piclist_info_title a'
    second_css = '::attr(title)'
    count_limit = 10


class IqiyiWebTvSpider(IqiyiWebZySpider):
    desc = u"[爱奇艺首页]电视剧"
    info = u"首页>电视剧(所有)"
    name = "iqiyi_web__tv"
    allowed_domains = ["www.iqiyi.com"]
    start_urls = (
        'http://www.iqiyi.com/',
    )
    first_css = 'div#block-O div.site-main-outer div.mod-listTitle_left p.textOverflow'
    second_css = '::text'
    count_limit = 1000


class IqiyiWebAnimationSpider(IqiyiWebZySpider):
    desc = u"[爱奇艺首页]动漫"
    info = u"首页>动漫(所有)"
    name = "iqiyi_web__dm"
    allowed_domains = ["www.iqiyi.com"]
    start_urls = (
        'http://www.iqiyi.com/',
    )
    first_css = 'div#block-P div.site-piclist_info p.site-piclist_info_title a'
    second_css = '::text'
    count_limit = 1000


class IqiyiWebVmovieSpider(IqiyiWebZySpider):
    desc = u"[爱奇艺首页]微电影"
    info = u"首页>微电影(所有)"
    name = "iqiyi_web__vmovie"
    allowed_domains = ["www.iqiyi.com"]
    start_urls = (
        'http://www.iqiyi.com/',
    )
    first_css = 'div#block-M div.site-piclist_info p.site-piclist_info_title a'
    second_css = '::text'
    count_limit = 1000


