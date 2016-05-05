# -*- coding: utf-8 -*-
import scrapy

from kuwo_scrapy.items import KuwoScrapyItem
from kuwo_scrapy.pipelines import KuwoScrapyDBConnector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst
from scrapy.exceptions import *

class BaiduNewAlbumSpider(scrapy.Spider):
    desc = u"[百度音乐首页]新碟首发"
    info = u"首页>首发，前6张专辑。"
    name = "baidu__new_album"
    allowed_domains = ["music.baidu.com"]
    start_urls = (
        'http://music.baidu.com/',
    )

    filte_css = '[monkey="NI_new_album"] div.mui-slider-scroll-container li'
    name_css = 'div.music a::text'
    artist_css = 'div.artist a::text'
    
    count_limit = 6
    
    def parse(self, response):
        try:
            new_albums = response.css(self.filte_css)
        except Exception,e:
            err = self.name + ':' + str(e)
            raise CloseSpider(err)

        count = 0
        for new_album in new_albums:
            count += 1
            if count > self.count_limit:
                raise CloseSpider('done')

            loader = ItemLoader(KuwoScrapyItem(), new_album)
            loader.add_value('basic_source_info', '{}')
            loader.add_css('basic_source_name', self.name_css, TakeFirst())
            loader.add_css('basic_source_artist', self.artist_css, Join('&'))
            yield loader.load_item()


class BaiduNewSongSpider(scrapy.Spider):
    desc = u"[百度音乐首页]新歌榜"
    info = u"首页>新歌榜,前10首。"
    name = "baidu__new_song"
    allowed_domains = ["music.baidu.com"]
    start_urls = (
        'http://music.baidu.com/',
    )
    
    first_css = '[monkey="NI_billboard_new"] ul.song-list div.song-info div.info'
    count_limit = 10

    def parse(self, response):
        try:
            new_songs = response.css(self.first_css)
        except Exception,e:
            err = self.name + ':' + str(e)
            raise CloseSpider(err)

        count = 0
        for new_song in new_songs:
            count += 1
            if count > self.count_limit:
                raise CloseSpider('done')

            loader = ItemLoader(KuwoScrapyItem(), new_song)
            loader.add_value('basic_source_info', '{}')
            loader.add_css('basic_source_name', 'div.song a::attr(title)', TakeFirst())
            loader.add_css('basic_source_artist', 'div.artist span::attr(title)', Join('&'))
            yield loader.load_item()


class BaiduLosslessAlbumSpider(BaiduNewAlbumSpider):
    desc = u"[百度音乐_音质提升]本周热卖无损大碟"
    info = u"音乐库>无损专区>本周热卖无损大碟，10张专辑更新提醒；"
    name = "baidu__lossless_hot_album"
    allowed_domains = ["music.baidu.com"]
    start_urls = (
        'http://music.baidu.com/lossless',
    )
    
    filte_css = 'div.module-lossless-sale div.body li div.list-title'
    name_css = 'a::text'
    artist_css = 'none'
    
    count_limit = 10


class BaiduLosslessNewAlbumAllSpider(BaiduNewAlbumSpider):
    desc = u"[百度音乐_音质提升]无损专区"
    info = u"音乐库>无损专区>全部专辑>>排序(时间)，16张专辑更新提醒；"
    name = "baidu__lossless_new_album_all"
    allowed_domains = ["music.baidu.com"]
    start_urls = (
        'http://music.baidu.com/lossless',
    )
    
    filte_css = 'div.main-body ul.albumlist li.album-item'
    name_css = 'div.album-name a::attr(title)'
    artist_css = 'div.singer-name a::text'
    
    count_limit = 16


