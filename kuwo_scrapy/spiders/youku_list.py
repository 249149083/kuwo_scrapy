# -*- coding: utf-8 -*-
import scrapy

from kuwo_scrapy.items import KuwoScrapyItem
from kuwo_scrapy.pipelines import KuwoScrapyDBConnector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst
from scrapy.exceptions import *

class YoukuListMovieLastestSpider(scrapy.Spider):
    desc = u"[优酷_电影]最近上映"
    info = u"分类(电影)>地区(全部)>类型(全部)>时间(全部)>状态(全部)>付费(全部)>排序(最近上映)"
    name = "youku_list__movie"
    allowed_domains = ["www.youku.com"]
    start_urls = (
        'http://www.youku.com/v_olist/c_96_s_5_d_1.html',
    )
    first_css = 'div#listofficial div.p-meta-title a'
    second_css = '::attr(title)'
    count_limit = 42
    
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


class YoukuListTvLastestSpider(YoukuListMovieLastestSpider):
    desc = u"[优酷_电视剧]最近上映"
    info = u"分类(电视剧)>地区(全部)>类型(全部)>时间(全部)>状态(全部)>付费(全部)>排序(最近上映)"
    name = "youku_list__tv"
    allowed_domains = ["www.youku.com"]
    start_urls = (
        'http://www.youku.com/v_olist/c_97_s_5_d_1.html',
    )
    first_css = 'div#listofficial div.p-meta-title a'
    second_css = '::attr(title)'
    count_limit = 42


class YoukuListAnimatinoLastestSpider(YoukuListMovieLastestSpider):
    desc = u"[优酷_动漫]最近上映"
    info = u"分类(动漫)>地区(全部)>类型(全部)>时间(全部)>状态(全部)>付费(全部)>排序(最近上映)"
    name = "youku_list__dm"
    allowed_domains = ["www.youku.com"]
    start_urls = (
        'http://www.youku.com/v_olist/c_100_s_5_d_1.html',
    )
    first_css = 'div#listofficial div.p-meta-title a'
    second_css = '::attr(title)'
    count_limit = 42


class YoukuListZyLastestSpider(YoukuListMovieLastestSpider):
    desc = u"[优酷_综艺]最近上映"
    info = u"分类(综艺)>地区(全部)>类型(全部)>时间(全部)>状态(全部)>付费(全部)>排序(最近上映)"
    name = "youku_list__zy"
    allowed_domains = ["www.youku.com"]
    start_urls = (
        'http://www.youku.com/v_olist/c_85_s_5_d_1.html',
    )
    first_css = 'div#listofficial div.p-meta-title a'
    second_css = '::attr(title)'
    count_limit = 42


class YoukuListVMovieLastestSpider(YoukuListMovieLastestSpider):
    desc = u"[优酷_微电影]最近上映"
    info = u"分类(微电影)>地区(全部)>类型(全部)>时间(全部)>状态(全部)>付费(全部)>排序(最新发布)，每种分类前42部。"
    name = "youku_list__vmovie"
    allowed_domains = ["www.youku.com"]
    start_urls = (
        'http://www.youku.com/v_showlist/c171d1s2.html',
    )

    first_css = 'div#getVideoList div.v div.v-meta div.v-meta-title a'
    second_css = '::attr(title)'
    count_limit = 42
