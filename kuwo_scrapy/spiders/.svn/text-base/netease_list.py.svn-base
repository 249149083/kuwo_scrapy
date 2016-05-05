# -*- coding: utf-8 -*-
import scrapy

from kuwo_scrapy.items import KuwoScrapyItem
from kuwo_scrapy.pipelines import KuwoScrapyDBConnector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst
from scrapy.exceptions import *

class NeteaseListNewMusic(scrapy.Spider):
    desc = u"[网易云音乐]云音乐新歌榜"
    info = u"首页>榜单>云音乐新歌榜（点击“查看全部”，97首）"
    name = "netease_list__new_music"
    allowed_domains = ["music.163.com"]
    start_urls = (
        'http://music.163.com/discover/toplist?id=3779629',
    )

    filter_css = 'tbody#tracklist tr[id^="songlist"]'
    name_css = 'span.txt a[href^="/song?id="]::text'
    artist_css = 'div.text a.s-fc3::text'
    
    count_limit = 97

    
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
            loader.add_css('basic_source_artist', self.artist_css, Join('&'))
            yield loader.load_item()


class NeteaseListNewOrgMusic(NeteaseListNewMusic):
    desc = u"[网易云音乐]网易原创歌曲榜"
    info = u"首页>榜单>网易原创歌曲榜（点击“查看全部”，97首）。"
    name = "netease_list__new_org_music"
    allowed_domains = ["music.163.com"]
    start_urls = (
        'http://music.163.com/discover/toplist?id=2884035',
    )

    filter_css = 'tbody#tracklist tr[id^="songlist"]'
    name_css = 'span.txt a[href^="/song?id="]::text'
    artist_css = 'div.text a.s-fc3::text'
    
    count_limit = 97
