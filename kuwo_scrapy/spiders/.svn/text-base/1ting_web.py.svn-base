# -*- coding: utf-8 -*-
import scrapy

from kuwo_scrapy.items import KuwoScrapyItem
from kuwo_scrapy.pipelines import KuwoScrapyDBConnector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst
from scrapy.exceptions import *

class OtingWebAlbumExSpider(scrapy.Spider):
    desc = u"[1ting首页]推荐专辑_精选"
    info = u"1ting首页>精选,8张专辑"
    name = "oting_web__album_ex"
    allowed_domains = ["www.1ting.com"]
    start_urls = (
        'http://www.1ting.com/',
    )
    filters = [
        {'css':'div.albumList ul:nth-child(1) li', 'limit' : 8}
    ]
    name_css = 'a.albumName::attr(title)'
    artist_css = 'a.singerName::attr(title)'
    
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


class OtingWebAlbumZhSpider(OtingWebAlbumExSpider):
    desc = u"[1ting首页]推荐专辑_华语"
    info = u"1ting首页>推荐专辑>华语"
    name = "oting_web__album_zh"
    allowed_domains = ["www.1ting.com"]
    start_urls = (
        'http://www.1ting.com/',
    )

    filters = [
        {'css':'div.albumList ul:nth-child(2) li', 'limit' : 8},
    ]

    name_css = 'a.albumName::attr(title)'
    artist_css = 'a.singerName::attr(title)'

class OtingWebAlbumEaSpider(OtingWebAlbumExSpider):
    desc = u"[1ting首页]推荐专辑_欧美"
    info = u"1ting首页>推荐专辑>欧美"
    name = "oting_web__album_ea"
    allowed_domains = ["www.1ting.com"]
    start_urls = (
        'http://www.1ting.com/',
    )

    filters = [
        {'css':'div.albumList ul:nth-child(3) li', 'limit' : 8},
    ]

    name_css = 'a.albumName::attr(title)'
    artist_css = 'a.singerName::attr(title)'

class OtingWebAlbumJkSpider(OtingWebAlbumExSpider):
    desc = u"[1ting首页]推荐专辑_日韩"
    info = u"1ting首页>推荐专辑>日韩"
    name = "oting_web__album_jk"
    allowed_domains = ["www.1ting.com"]
    start_urls = (
        'http://www.1ting.com/',
    )

    filters = [
        {'css':'div.albumList ul:nth-child(4) li', 'limit' : 8}
    ]

    name_css = 'a.albumName::attr(title)'
    artist_css = 'a.singerName::attr(title)'


class OtingWebMusicZhSpider(OtingWebAlbumExSpider):
    desc = u"[1ting首页]新歌推荐_华语"
    info = u"1ting首页>新歌推荐>华语"
    name = "oting_web__music_zh"
    allowed_domains = ["www.1ting.com"]
    start_urls = (
        'http://www.1ting.com/',
    )
    filters = [
        {'css':'div#newSongList ul:nth-child(1) li', 'limit' : 20},
        {'css':'div#newSongList ul:nth-child(2) li', 'limit' : 20},
        {'css':'div#newSongList ul:nth-child(3) li', 'limit' : 20},
    ]

    name_css = 'a.songTitle::text'
    artist_css = 'a.singerName::text'


class OtingWebMusicEaSpider(OtingWebAlbumExSpider):
    desc = u"[1ting首页]新歌推荐_欧美"
    info = u"1ting首页>新歌推荐>欧美"
    name = "oting_web__music_ea"
    allowed_domains = ["www.1ting.com"]
    start_urls = (
        'http://www.1ting.com/',
    )
    filters = [
        {'css':'div#newSongList ul:nth-child(2) li', 'limit' : 20},
    ]

    name_css = 'a.songTitle::text'
    artist_css = 'a.singerName::text'


class OtingWebMusicJkSpider(OtingWebAlbumExSpider):
    desc = u"[1ting首页]新歌推荐_日韩"
    info = u"1ting首页>新歌推荐>日韩"
    name = "oting_web__music_jk"
    allowed_domains = ["www.1ting.com"]
    start_urls = (
        'http://www.1ting.com/',
    )
    filters = [
        {'css':'div#newSongList ul:nth-child(3) li', 'limit' : 20},
    ]

    name_css = 'a.songTitle::text'
    artist_css = 'a.singerName::text'


class OtingWebNewAlbumSpider(OtingWebAlbumExSpider):
    desc = u"[1ting]最新专辑"
    info = u"排行榜 - 最新专辑>全部>最新专辑，前20张专辑。"
    name = "oting_web__new_album"
    allowed_domains = ["www.1ting.com"]
    start_urls = (
        'http://www.1ting.com/album_n.html',
    )
    filters = [
        {'css':'div.albumList ul.albumUL li', 'limit' : 20},
    ]

    name_css = 'span.albumName::text'
    artist_css = 'span.singerName a::text'

