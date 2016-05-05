# -*- coding: utf-8 -*-
import scrapy

from kuwo_scrapy.items import KuwoScrapyItem
from kuwo_scrapy.pipelines import KuwoScrapyDBConnector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst
from scrapy.exceptions import *

class FSingWebOrgSpider(scrapy.Spider):
    desc = u"[5sing首页]原创推荐"
    info = u"5sing首页>原创推荐"
    name = "fsing_web__org"
    allowed_domains = ["5sing.kugou.com"]
    start_urls = (
        'http://5sing.kugou.com/index.html',
    )

    filter_css = 'div.song_yc div.yc_list dl'
    name_css = 'strong.sl_name a::attr(title)'
    artist_css = 'dd.s1_d1 a::text'
    
    count_limit = 999

    
    def parse(self, response):
        try:
            movies = response.css(self.filter_css)
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


class FSingWebCpySpider(FSingWebOrgSpider):
    desc = u"[5sing首页]翻唱推荐"
    info = u"5sing首页>翻唱推荐"
    name = "fsing_web__cpy"
    allowed_domains = ["5sing.kugou.com"]
    start_urls = (
        'http://5sing.kugou.com/index.html',
    )

    filter_css = 'div.song_fc div.yc_list dl'
    name_css = 'strong.sl_name a::attr(title)'
    artist_css = 'dd.s1_d1 a::text'
    
    count_limit = 999
