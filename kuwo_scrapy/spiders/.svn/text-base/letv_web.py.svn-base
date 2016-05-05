# -*- coding: utf-8 -*-
import scrapy

from kuwo_scrapy.items import KuwoScrapyItem
from kuwo_scrapy.pipelines import KuwoScrapyDBConnector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst
from scrapy.exceptions import *

class LetvWebMovieSpider(scrapy.Spider):
    desc = u"[乐视首页]电影"
    info = u"首页>电影会员（10部）"
    name = "letv_web__movie"
    allowed_domains = ["www.letv.com"]
    start_urls = (
        'http://www.letv.com/',
    )
    first_css = 'div.movie_vip .d_tit a'
    second_css = '::attr(title)'
    count_limit = 10
    
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


class LetvWebZySpider(LetvWebMovieSpider):
    desc = u"[乐视首页]综艺"
    info = u"首页>综艺（12部）"
    name = "letv_web__zy"
    allowed_domains = ["www.letv.com"]
    start_urls = (
        'http://www.letv.com/',
    )
    first_css = 'div.zongyi .d_tit a'
    second_css = '::attr(title)'
    count_limit = 12


class LetvWebTvSpider(LetvWebMovieSpider):
    desc = u"[乐视首页]电视剧"
    info = u"首页>电视剧（12部）"
    name = "letv_web__tv"
    allowed_domains = ["www.letv.com"]
    start_urls = (
        'http://www.letv.com/',
    )
    first_css = 'div.tv .d_tit a'
    second_css = '::attr(title)'
    count_limit = 12


class LetvWebAnimationSpider(scrapy.Spider):
    desc = u"[乐视首页]动漫"
    info = u"首页>动漫（7部）"
    name = "letv_web__dm"
    allowed_domains = ["www.letv.com"]
    start_urls = (
        'http://www.letv.com/',
    )
    count_limit = 7


    def parse(self, response):
        try:
            movies = response.xpath('//body/div[@class="column61"]').css('.d_tit a')
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
            loader.add_css('basic_source_name', '::attr(title)', Join())
            loader.add_value('basic_source_artist', '')
            yield loader.load_item()
