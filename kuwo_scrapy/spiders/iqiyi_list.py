# -*- coding: utf-8 -*-
import scrapy

from kuwo_scrapy.items import KuwoScrapyItem
from kuwo_scrapy.pipelines import KuwoScrapyDBConnector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst
from scrapy.exceptions import *

class IqiyiListMovieSpider(scrapy.Spider):
    desc = u"[爱奇艺_电影]更新"
    info = u"频道(电影)>地区(全部)>分类(全部)>年代(全部)>排序(更新时间、全网)，前30部。"
    name = "iqiyi_list__movie"
    allowed_domains = ["list.iqiyi.com"]
    start_urls = (
        'http://list.iqiyi.com/www/1/-------------4-1-1---.html',
    )
    first_css = 'div.page-list div.site-main p.site-piclist_info_title a'
    
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


class IqiyiListTvSpider(IqiyiListMovieSpider):
    desc = u"[爱奇艺_电视剧]更新"
    info = u"频道(电视剧)>地区(全部)>分类(全部)>年代(全部)>排序(更新时间、全网)，前30部。"
    name = "iqiyi_list__tv"
    allowed_domains = ["list.iqiyi.com"]
    start_urls = (
        'http://list.iqiyi.com/www/2/-------------4-1-1---.html',
    )
    first_css = 'div.page-list div.site-main p.site-piclist_info_title a'


class IqiyiListAnimationSpider(IqiyiListMovieSpider):
    desc = u"[爱奇艺_动漫]更新"
    info = u"频道(动漫)>地区(全部)>分类(全部)>年代(全部)>排序(更新时间、全网)，前30部。"
    name = "iqiyi_list__dm"
    allowed_domains = ["list.iqiyi.com"]
    start_urls = (
        'http://list.iqiyi.com/www/4/-------------4-1-1---.html',
    )
    first_css = 'div.page-list div.site-main p.site-piclist_info_title a'


class IqiyiListZySpider(IqiyiListMovieSpider):
    desc = u"[爱奇艺_综艺]更新"
    info = u"频道(综艺)>地区(全部)>分类(全部)>年代(全部)>排序(更新时间、全网)，前30部。"
    name = "iqiyi_list__zy"
    allowed_domains = ["list.iqiyi.com"]
    start_urls = (
        'http://list.iqiyi.com/www/6/-------------4-1-1---.html',
    )
    first_css = 'div.page-list div.site-main p.site-piclist_info_title a'
