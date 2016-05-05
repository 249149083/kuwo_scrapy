# -*- coding: utf-8 -*-
import json
import scrapy

from kuwo_scrapy.items import KuwoScrapyItem
from kuwo_scrapy.pipelines import KuwoScrapyDBConnector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst
from scrapy.exceptions import *

class YinyuetaiMvShouboAllSpider(scrapy.Spider):
    desc = u"[音悦台_首播]改变通知"
    info = u"音悦台首页，MV首播>全部，标签下33个视频"
    name = "yinyuetai__mv_shoubo_all"
    allowed_domains = ["yinyuetai.com"]
    start_urls = (
        'http://www.yinyuetai.com/ajax/shoubo?area=all',
    )

    def parse(self, response):
        try:
            mvs = json.loads(response.body)
        except Exception,e:
            err = self.name + ':' + str(e)
            raise CloseSpider(err)

        count = 0
        for mv in mvs:
            count += 1
            if count > 33:
                raise CloseSpider('done')

            item = KuwoScrapyItem()
            item['basic_source_info'] = '{}'
            item['basic_source_name'] = mv['title']
            item['basic_source_artist'] = '&'.join([m['artistName'] for m in mv['artists']])
            yield item


class YinyuetaiMvShouboHtSpider(YinyuetaiMvShouboAllSpider):
    desc = u"[音悦台_港台]改变通知"
    info = u"音悦台首页，MV首播>港台，标签下33个视频"
    name = "yinyuetai__mv_shoubo_ht"
    allowed_domains = ["yinyuetai.com"]
    start_urls = (
        'http://www.yinyuetai.com/ajax/shoubo?area=ht',
    )

class YinyuetaiMvShouboMlSpider(YinyuetaiMvShouboAllSpider):
    desc = u"[音悦台_内地]改变通知"
    info = u"音悦台首页，MV首播>内地，标签下33个视频"
    name = "yinyuetai__mv_shoubo_ml"
    allowed_domains = ["yinyuetai.com"]
    start_urls = (
        'http://www.yinyuetai.com/ajax/shoubo?area=ml',
    )

class YinyuetaiMvShouboUsSpider(YinyuetaiMvShouboAllSpider):
    desc = u"[音悦台_欧美]改变通知"
    info = u"音悦台首页，MV首播>欧美，标签下33个视频"
    name = "yinyuetai__mv_shoubo_us"
    allowed_domains = ["yinyuetai.com"]
    start_urls = (
        'http://www.yinyuetai.com/ajax/shoubo?area=us',
    )

class YinyuetaiMvShouboKrSpider(YinyuetaiMvShouboAllSpider):
    desc = u"[音悦台_韩国]改变通知"
    info = u"音悦台首页，MV首播>韩国，标签下33个视频"
    name = "yinyuetai__mv_shoubo_kr"
    allowed_domains = ["yinyuetai.com"]
    start_urls = (
        'http://www.yinyuetai.com/ajax/shoubo?area=kr',
    )

class YinyuetaiMvShouboJpSpider(YinyuetaiMvShouboAllSpider):
    desc = u"[音悦台_日本]改变通知"
    info = u"音悦台首页，MV首播>日本，标签下33个视频"
    name = "yinyuetai__mv_shoubo_jp"
    allowed_domains = ["yinyuetai.com"]
    start_urls = (
        'http://www.yinyuetai.com/ajax/shoubo?area=jp',
    )


