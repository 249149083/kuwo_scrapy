# -*- coding: utf-8 -*-
import scrapy

from kuwo_scrapy.items import KuwoScrapyItem
from kuwo_scrapy.pipelines import KuwoScrapyDBConnector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst
from scrapy.exceptions import *

class DoubanWebMovieNowplayingSpider(scrapy.Spider):
    desc = u"[豆瓣_电影]正在上映"
    info = u"豆瓣电影>电影票>正在上映,全部。"
    name = "douban_web__movie_nowplaying"
    allowed_domains = ["movie.douban.com"]
    start_urls = (
        'http://movie.douban.com/nowplaying/beijing/',
    )
    first_css = 'div#nowplaying li[data-title]'
    second_css = '::attr(data-title)'
    count_limit = 999
    
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


class DoubanWebMovieUpcomingSpider(DoubanWebMovieNowplayingSpider):
    desc = u"[豆瓣_电影]即将上映"
    info = u"豆瓣电影>电影票>即将上映,全部。"
    name = "douban_web__movie_upcoming"
    allowed_domains = ["movie.douban.com"]
    start_urls = (
        'http://movie.douban.com/nowplaying/beijing/',
    )
    first_css = 'div#upcoming li[data-title]'
    second_css = '::attr(data-title)'
    count_limit = 999


class DoubanWebTvSpider(DoubanWebMovieNowplayingSpider):
    desc = u"[豆瓣_电视剧]豆瓣电视剧新片榜"
    info = u"豆瓣电影>电视剧>豆瓣电视剧新片榜，20部。"
    name = "douban_web__tv"
    allowed_domains = ["movie.douban.com"]
    start_urls = (
        'http://movie.douban.com/tv/',
    )
    first_css = 'tr.item a.nbg'
    second_css = '::attr(title)'
    count_limit = 20



