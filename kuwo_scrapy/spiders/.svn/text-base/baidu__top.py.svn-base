# -*- coding: utf-8 -*-
import scrapy

from kuwo_scrapy.items import KuwoScrapyItem
from kuwo_scrapy.pipelines import KuwoScrapyDBConnector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst
from scrapy.exceptions import *

class BaiduTopNewMovieSpider(scrapy.Spider):
    desc = u"[百度风云榜]电影榜"
    info = u"百度搜索风云榜>娱乐>电影，全部50部。"
    name = "baidu_top__new_movie"
    allowed_domains = ["top.baidu.com"]
    start_urls = (
        'http://top.baidu.com/buzz?b=26&c=1&fr=topcategory_c1',
    )
    
    def parse(self, response):
        try:
            movies = response.css('div.grayborder table.list-table a.list-title')
        except Exception,e:
            err = self.name + ':' + str(e)
            raise CloseSpider(err)

        count = 0
        for movie in movies:
            count += 1
            if count > 50:
                raise CloseSpider('done')

            loader = ItemLoader(KuwoScrapyItem(), movie)
            loader.add_value('basic_source_info', '{}')
            loader.add_css('basic_source_name', '::text', Join())
            loader.add_value('basic_source_artist', '')
            yield loader.load_item()


class BaiduTopNewTvSpider(BaiduTopNewMovieSpider):
    desc = u"[百度风云榜]电视剧榜"
    info = u"百度搜索风云榜>娱乐>电视剧，全部50部。"
    name = "baidu_top__new_tv"
    allowed_domains = ["top.baidu.com"]
    start_urls = (
        'http://top.baidu.com/buzz?b=4&c=2&fr=topcategory_c2',
    )


class BaiduTopNewAnimationSpider(BaiduTopNewMovieSpider):
    desc = u"[百度风云榜]动漫榜"
    info = u"百度搜索风云榜>娱乐>动漫，全部50部。"
    name = "baidu_top__new_dm"
    allowed_domains = ["top.baidu.com"]
    start_urls = (
        'http://top.baidu.com/buzz?b=23&c=5&fr=topcategory_c5',
    )


class BaiduTopNewZySpider(BaiduTopNewMovieSpider):
    desc = u"[百度风云榜]综艺榜"
    info = u"百度搜索风云榜>娱乐>综艺，全部50部。"
    name = "baidu_top__new_zy"
    allowed_domains = ["top.baidu.com"]
    start_urls = (
        'http://top.baidu.com/buzz?b=19&c=3&fr=topcategory_c3',
    )
