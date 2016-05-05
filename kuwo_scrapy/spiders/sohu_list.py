# -*- coding: utf-8 -*-
import scrapy

from kuwo_scrapy.items import KuwoScrapyItem
from kuwo_scrapy.pipelines import KuwoScrapyDBConnector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst
from scrapy.exceptions import *

class SohuListMovieLastestSpider(scrapy.Spider):
    desc = u"[搜狐_电影]最新"
    info = u"精选(电影)>类别(全部)>地区(全部)>最新(全网)，前30部。"
    name = "sohu_list__movie"
    allowed_domains = ["so.tv.sohu.com"]
    start_urls = (
        'http://so.tv.sohu.com/list_p1100_p2_p3_p4_p5_p6_p73_p8_p9_p10_p11_p12_p131.html',
    )
    first_css = 'ul.st-list strong a'
    second_css = '::attr(title)'
    count_limit = 30
    
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


class SohuListTvLastestSpider(SohuListMovieLastestSpider):
    desc = u"[搜狐_电视剧]最新"
    info = u"精选(电视剧)>类别(全部)>地区(全部)>最新(全网)，前30部。"
    name = "sohu_list__tv"
    allowed_domains = ["so.tv.sohu.com"]
    start_urls = (
        'http://so.tv.sohu.com/list_p1101_p2_p3_p4_p5_p6_p73_p8_p9_p10_p11_p12_p13.html',
    )
    first_css = 'ul.st-list strong a'
    second_css = '::attr(title)'
    count_limit = 30


class SohuListZyLastestSpider(SohuListMovieLastestSpider):
    desc = u"[搜狐_综艺]最新"
    info = u"精选(综艺)>类别(全部)>地区(全部)>最新(全网)，前30部。"
    name = "sohu_list__zy"
    allowed_domains = ["so.tv.sohu.com"]
    start_urls = (
        'http://so.tv.sohu.com/list_p1106_p2_p3_p4_p5_p6_p73_p8_p9_p10_p11_p12_p13.html',
    )
    first_css = 'ul.st-list strong a'
    second_css = '::attr(title)'
    count_limit = 30



class SohuListAnimationLastestSpider(SohuListMovieLastestSpider):
    desc = u"[搜狐_动漫]最新"
    info = u"精选(动漫)>类别(全部)>地区(全部)>最新(全网)，前30部。"
    name = "sohu_list__dm"
    allowed_domains = ["so.tv.sohu.com"]
    start_urls = (
        'http://so.tv.sohu.com/list_p1115_p2_p3_p4_p5_p6_p73_p8_p9_p10_p11_p12_p13.html',
    )
    first_css = 'ul.st-list strong a'
    second_css = '::attr(title)'
    count_limit = 30
