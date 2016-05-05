# -*- coding: utf-8 -*-
import json
import scrapy

from kuwo_scrapy.items import KuwoScrapyItem
from kuwo_scrapy.pipelines import KuwoScrapyDBConnector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst
from scrapy.exceptions import *

class DoubanListHotSpider(scrapy.Spider):
    desc = u"[豆瓣_电影]选电影_热门"
    info = u"豆瓣电影>选电影>热门>按热度排序(按时间排序或按评价排序)，20部。"
    name = "douban_list__movie_hot"
    allowed_domains = ["movie.douban.com"]
    start_urls = (
        'http://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0',
    )

    def parse(self, response):
        try:
            info = json.loads(response.body)
            mvs = info['subjects']
        except Exception,e:
            err = self.name + ':' + str(e)
            raise CloseSpider(err)

        count = 0
        for mv in mvs:
            count += 1
            if count > 20:
                raise CloseSpider('done')

            item = KuwoScrapyItem()
            item['basic_source_info'] = '{}'
            item['basic_source_name'] = mv['title']
            item['basic_source_artist'] = ''
            yield item


class DoubanListNewSpider(DoubanListHotSpider):
    desc = u"[豆瓣_电影]选电影_最新"
    info = u"豆瓣电影>选电影>最新>按热度排序(按时间排序或按评价排序)，20部。"
    name = "douban_list__movie_new"
    allowed_domains = ["movie.douban.com"]
    start_urls = (
        'http://movie.douban.com/j/search_subjects?type=movie&tag=%E6%9C%80%E6%96%B0&page_limit=20&page_start=0',
    )


