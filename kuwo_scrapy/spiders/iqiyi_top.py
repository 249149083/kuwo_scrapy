# -*- coding: utf-8 -*-
import scrapy

from kuwo_scrapy.items import KuwoScrapyItem
from kuwo_scrapy.pipelines import KuwoScrapyDBConnector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst
from scrapy.exceptions import *

class IqiyiTopZySpider(scrapy.Spider):
    desc = u"[爱奇艺风云榜]综艺"
    info = u"风云榜>全部>综艺，前50部。"
    name = "iqiyi_top__zy"
    allowed_domains = ["top.iqiyi.com"]
    start_urls = (
        'http://top.iqiyi.com/zongyi.html#vfrm=7-13-0-1',
    )
    
    first_css = 'div#block-D div#tab_top50 ul.tv_list a[rseat^="bang1_"]'
    
    def parse(self, response):
        try:
            movies = response.css(self.first_css)
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
            loader.add_css('basic_source_name', '::attr(title)', Join())
            loader.add_value('basic_source_artist', '')
            yield loader.load_item()


class IqiyiTopTvSpider(IqiyiTopZySpider):
    desc = u"[爱奇艺风云榜]电视剧"
    info = u"风云榜>全部>电视剧，前50部。"
    name = "iqiyi_top__tv"
    allowed_domains = ["top.iqiyi.com"]
    start_urls = (
        'http://top.iqiyi.com/dianshiju.html#vfrm=7-13-0-1',
    )
    
    first_css = 'div#block-D div#tab_top50 ul.tv_list a[rseat^="bang1_"]'


class IqiyiTopAnimationSpider(IqiyiTopZySpider):
    desc = u"[爱奇艺风云榜]动漫"
    info = u"风云榜>全部>动漫，前50部。"
    name = "iqiyi_top__dm"
    allowed_domains = ["top.iqiyi.com"]
    start_urls = (
        'http://top.iqiyi.com/dongman.html#vfrm=7-13-0-1',
    )
    
    first_css = 'div#block-D div#tab_top50 ul.tv_list a[rseat^="bang1_"]'

class IqiyiTopMovieSpider(IqiyiTopZySpider):
    desc = u"[爱奇艺风云榜]电影"
    info = u"风云榜>全部>电影，前50部。"
    name = "iqiyi_top__movie"
    allowed_domains = ["top.iqiyi.com"]
    start_urls = (
        'http://top.iqiyi.com/dianying.html#vfrm=7-13-0-1',
    )
    
    first_css = 'div#block-D div#tab_top50 ul.tv_list a[rseat^="bang1_"]'

