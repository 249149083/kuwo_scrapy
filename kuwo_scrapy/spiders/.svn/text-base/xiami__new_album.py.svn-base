# -*- coding: utf-8 -*-
import scrapy

from kuwo_scrapy.items import KuwoScrapyItem
from kuwo_scrapy.pipelines import KuwoScrapyDBConnector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst
from scrapy.exceptions import *

class XiamiWebNewAlbumSpider(scrapy.Spider):
    desc = u"[虾米首页]新碟首发"
    info = u"虾米音乐首页>新碟首发(前10张专辑)"
    name = "xiami_web__new_album"
    allowed_domains = ["xiami.com"]
    start_urls = (
        'http://www.xiami.com/',
    )

    filter_css = 'div#albums div.album div.info'

    name_css = 'p.name strong a::attr(title)'
    artist_css = 'p a::attr(title)'

    count_limit = 10
    
    def parse(self, response):
        new_albums = response.css(self.filter_css)
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


class XiamiNewAlbumSpider(XiamiWebNewAlbumSpider):
    desc = u"[虾米]新碟上架"
    info = u"发现音乐>专辑>新碟上架(前14张专辑)"
    name = "xiami__new_album"
    allowed_domains = ["xiami.com"]
    start_urls = (
        'http://www.xiami.com/music/newalbum',
    )

    filter_css = 'div#albums div.album div.info'
    name_css = 'p:nth-child(1) a::attr(title)'
    artist_css = 'p:nth-child(2) a::attr(title)'

    count_limit = 14

