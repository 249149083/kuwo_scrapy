# -*- coding: utf-8 -*-
import scrapy

from kuwo_scrapy.items import KuwoScrapyItem
from kuwo_scrapy.pipelines import KuwoScrapyDBConnector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst
from scrapy.exceptions import *

class FSingListOrgLastestSpider(scrapy.Spider):
    desc = u"[5sing原创]最新上传"
    info = u"5sing首页>原创>最新上传"
    name = "fsing_list__org_lastest"
    allowed_domains = ["5sing.kugou.com"]
    start_urls = (
        'http://5sing.kugou.com/yc/index.html',
    )

    filter_css = 'div.con_lists:nth-child(4) div.w240 ul li'
    name_css = 'a.m_t::attr(title)'
    artist_css = 'a.m_z::attr(title)'
    
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
            loader.add_css('basic_source_name', self.name_css, TakeFirst())
            loader.add_css('basic_source_artist', self.artist_css, Join())
            yield loader.load_item()


class FSingListCpyLastestSpider(FSingListOrgLastestSpider):
    desc = u"[5sing翻唱]最新上传"
    info = u"5sing首页>翻唱>最新上传"
    name = "fsing_list__cpy_lastest"
    allowed_domains = ["5sing.kugou.com"]
    start_urls = (
        'http://5sing.kugou.com/fc/index.html',
    )

    filter_css = 'div.con_lists:nth-child(3) div.w240 ul li'
    name_css = 'a.m_t::attr(title)'
    artist_css = 'a.m_z::attr(title)'
    
    count_limit = 999


class FSingListOrgRecommendSpider(FSingListOrgLastestSpider):
    desc = u"[5sing原创]网友自荐"
    info = u"5sing首页>原创>网友自荐"
    name = "fsing_list__org_recommend"
    allowed_domains = ["5sing.kugou.com"]
    start_urls = (
        'http://5sing.kugou.com/yc/index.html',
    )

    filter_css = 'div#ScrollContent ul li'
    name_css = 'a.m_t::attr(title)'
    artist_css = 'a.m_z::attr(title)'
    
    count_limit = 999


class FSingListCpyRecommendSpider(FSingListOrgLastestSpider):
    desc = u"[5sing翻唱]网友自荐"
    info = u"5sing首页>翻唱>网友自荐"
    name = "fsing_list__cpy_recommend"
    allowed_domains = ["5sing.kugou.com"]
    start_urls = (
        'http://5sing.kugou.com/fc/index.html',
    )

    filter_css = 'div#ScrollContent ul li'
    name_css = 'a.m_t::attr(title)'
    artist_css = 'a.m_z::attr(title)'
    
    count_limit = 999


class FSingListOrgGoodZhSpider(FSingListOrgLastestSpider):
    desc = u"[5sing原创]优质原创_华语"
    info = u"5sing首页>原创>优质原创>华语"
    name = "fsing_list__org_good_zh"
    allowed_domains = ["5sing.kugou.com"]
    start_urls = (
        'http://5sing.kugou.com/yc/index.html',
    )

    filter_css = 'div.con_lists:nth-child(1) div.w710 ul li[name="glytj0"]'
    name_css = 'a.m_t::attr(title)'
    artist_css = 'a.m_z::attr(title)'
    
    count_limit = 999


class FSingListOrgGoodPopSpider(FSingListOrgLastestSpider):
    desc = u"[5sing原创]优质原创_流行"
    info = u"5sing首页>原创>优质原创>流行"
    name = "fsing_list__org_good_pop"
    allowed_domains = ["5sing.kugou.com"]
    start_urls = (
        'http://5sing.kugou.com/yc/index.html',
    )

    filter_css = 'div.con_lists:nth-child(1) div.w710 ul li[name="glytj0"]'
    name_css = 'a.m_t::attr(title)'
    artist_css = 'a.m_z::attr(title)'
    
    count_limit = 999


class FSingListOrgGoodClassicalSpider(FSingListOrgLastestSpider):
    desc = u"[5sing原创]优质原创_流行"
    info = u"5sing首页>原创>优质原创>流行"
    name = "fsing_list__org_good_classical"
    allowed_domains = ["5sing.kugou.com"]
    start_urls = (
        'http://5sing.kugou.com/yc/index.html',
    )

    filter_css = 'div.con_lists:nth-child(1) div.w710 ul li[name="glytj0"]'
    name_css = 'a.m_t::attr(title)'
    artist_css = 'a.m_z::attr(title)'
    
    count_limit = 999


class FSingListOrgGoodClassicalSpider(FSingListOrgLastestSpider):
    desc = u"[5sing原创]优质原创_古风"
    info = u"5sing首页>原创>优质原创>古风"
    name = "fsing_list__org_good_classical"
    allowed_domains = ["5sing.kugou.com"]
    start_urls = (
        'http://5sing.kugou.com/yc/index.html',
    )

    filter_css = 'div.con_lists:nth-child(1) div.w710 ul li[name="glytj1"]'
    name_css = 'a.m_t::attr(title)'
    artist_css = 'a.m_z::attr(title)'
    
    count_limit = 999


class FSingListOrgGoodRNRSpider(FSingListOrgLastestSpider):
    desc = u"[5sing原创]优质原创_摇滚&说唱"
    info = u"5sing首页>原创>优质原创>摇滚&说唱"
    name = "fsing_list__org_good_rnr"
    allowed_domains = ["5sing.kugou.com"]
    start_urls = (
        'http://5sing.kugou.com/yc/index.html',
    )

    filter_css = 'div.con_lists:nth-child(1) div.w710 ul li[name="glytj2"]'
    name_css = 'a.m_t::attr(title)'
    artist_css = 'a.m_z::attr(title)'
    
    count_limit = 999


class FSingListOrgGoodMNMSpider(FSingListOrgLastestSpider):
    desc = u"[5sing原创]优质原创_民族&美声"
    info = u"5sing首页>原创>优质原创>民族&美声"
    name = "fsing_list__org_good_mnm"
    allowed_domains = ["5sing.kugou.com"]
    start_urls = (
        'http://5sing.kugou.com/yc/index.html',
    )

    filter_css = 'div.con_lists:nth-child(1) div.w710 ul li[name="glytj3"]'
    name_css = 'a.m_t::attr(title)'
    artist_css = 'a.m_z::attr(title)'
    
    count_limit = 999


class FSingListCpyGoodZhSpider(FSingListOrgLastestSpider):
    desc = u"[5sing翻唱]优质翻唱_华语"
    info = u"5sing首页>翻唱>优质翻唱_华语"
    name = "fsing_list__cpy_good_zh"
    allowed_domains = ["5sing.kugou.com"]
    start_urls = (
        'http://5sing.kugou.com/fc/index.html',
    )

    filter_css = 'div.con_lists:nth-child(1) div.w710 ul li[name="glytj0"]'
    name_css = 'a.m_t::attr(title)'
    artist_css = 'a.m_z::attr(title)'
    
    count_limit = 999


class FSingListCpyGoodClassicalSpider(FSingListOrgLastestSpider):
    desc = u"[5sing翻唱]优质翻唱_古风"
    info = u"5sing首页>翻唱>优质翻唱_古风"
    name = "fsing_list__cpy_good_classical"
    allowed_domains = ["5sing.kugou.com"]
    start_urls = (
        'http://5sing.kugou.com/fc/index.html',
    )

    filter_css = 'div.con_lists:nth-child(1) div.w710 ul li[name="glytj1"]'
    name_css = 'a.m_t::attr(title)'
    artist_css = 'a.m_z::attr(title)'
    
    count_limit = 999


class FSingListCpyGoodEaSpider(FSingListOrgLastestSpider):
    desc = u"[5sing翻唱]优质翻唱_欧美"
    info = u"5sing首页>翻唱>优质翻唱_欧美"
    name = "fsing_list__cpy_good_ea"
    allowed_domains = ["5sing.kugou.com"]
    start_urls = (
        'http://5sing.kugou.com/fc/index.html',
    )

    filter_css = 'div.con_lists:nth-child(1) div.w710 ul li[name="glytj2"]'
    name_css = 'a.m_t::attr(title)'
    artist_css = 'a.m_z::attr(title)'
    
    count_limit = 999


class FSingListCpyGoodJpSpider(FSingListOrgLastestSpider):
    desc = u"[5sing翻唱]优质翻唱_日语"
    info = u"5sing首页>翻唱>优质翻唱_日语"
    name = "fsing_list__cpy_good_jp"
    allowed_domains = ["5sing.kugou.com"]
    start_urls = (
        'http://5sing.kugou.com/fc/index.html',
    )

    filter_css = 'div.con_lists:nth-child(1) div.w710 ul li[name="glytj3"]'
    name_css = 'a.m_t::attr(title)'
    artist_css = 'a.m_z::attr(title)'
    
    count_limit = 999


class FSingListCpyGoodKrSpider(FSingListOrgLastestSpider):
    desc = u"[5sing翻唱]优质翻唱_韩语"
    info = u"5sing首页>翻唱>优质翻唱_韩语"
    name = "fsing_list__cpy_good_kr"
    allowed_domains = ["5sing.kugou.com"]
    start_urls = (
        'http://5sing.kugou.com/fc/index.html',
    )

    filter_css = 'div.con_lists:nth-child(1) div.w710 ul li[name="glytj4"]'
    name_css = 'a.m_t::attr(title)'
    artist_css = 'a.m_z::attr(title)'
    
    count_limit = 999


class FSingListBzLastestSpider(FSingListOrgLastestSpider):
    desc = u"[5sing伴奏]最新上传"
    info = u"5sing首页>伴奏>最新上传"
    name = "fsing_list__bz_lastest"
    allowed_domains = ["5sing.kugou.com"]
    start_urls = (
        'http://5sing.kugou.com/bz/index.shtml',
    )

    filter_css = 'div.bz_new:nth-child(1) ul li'
    name_css = 'a.bz_new_a::attr(title)'
    artist_css = 'a.c999::attr(title)'
    
    count_limit = 999
