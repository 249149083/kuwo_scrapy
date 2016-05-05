# -*- coding: utf-8 -*-
import scrapy

from kuwo_scrapy.items import KuwoScrapyItem
from kuwo_scrapy.pipelines import KuwoScrapyDBConnector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst
from scrapy.exceptions import *

class LetvListMovieSpider(scrapy.Spider):
    desc = u"[乐视_电影]最新更新"
    info = u"电影>电影>最新更新(昨日热播、历史热播、最高评分)"
    name = "letv_list__movie"
    allowed_domains = ["list.letv.com"]
    start_urls = (
        'http://list.letv.com/listn/c1_t-1_a-1_y-1_s1_lg-1_ph-1_md_o4_d1_p.html',
        'http://list.letv.com/listn/c1_t-1_a-1_y-1_s1_lg-1_ph-1_md_o9_d1_p.html',
        'http://list.letv.com/listn/c1_t-1_a-1_y-1_s1_lg-1_ph-1_md_o3_d1_p.html',
        'http://list.letv.com/listn/c1_t-1_a-1_y-1_s1_lg-1_ph-1_md_o2_d1_p.html',
    )

    filters = [
        {'css': 'div.list_seo p.p_t a', 'limit': 999}
    ]
    name_css = '::attr(title)'
    artist_css = 'none'

    def parse(self, response):
        try:
            for f in self.filters:
                f['sels'] = response.css(f['css'])

        except Exception,e:
            err = self.name + ':' + str(e)
            raise CloseSpider(err)

        count = 0
        c_index = -1
        for f in self.filters:
            sels = f['sels']
            for sel in sels:
                if count > f['limit']:
                    break
                loader = ItemLoader(KuwoScrapyItem(), sel)
                loader.add_value('basic_source_info', '{}')
                loader.add_css('basic_source_name', self.name_css, Join())
                loader.add_css('basic_source_artist', self.artist_css, Join())
                yield loader.load_item()


class LetvListTvLastestSpider(LetvListMovieSpider):
    desc = u"[乐视_电视剧]最新更新"
    info = u"电视剧>最新更新(昨日热播、历史热播、最高评分)"
    name = "letv_list__tv"
    allowed_domains = ["list.letv.com"]
    start_urls = (
        'http://list.letv.com/listn/c2_t-1_a-1_y-1_s1_md_o51_d1_p.html',
        'http://list.letv.com/listn/c2_t-1_a-1_y-1_s1_md_o9_d1_p.html',
        'http://list.letv.com/listn/c2_t-1_a-1_y-1_s1_md_o3_d1_p.html',
        'http://list.letv.com/listn/c2_t-1_a-1_y-1_s1_md_o2_d1_p.html',
    )


