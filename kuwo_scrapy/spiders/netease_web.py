# -*- coding: utf-8 -*-
import json
import scrapy

from kuwo_scrapy.items import KuwoScrapyItem
from kuwo_scrapy.pipelines import KuwoScrapyDBConnector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst
from scrapy.http import Request
from scrapy.exceptions import *



class NeteaseWebNewAlbumSpider(scrapy.Spider):
    desc = u"[网易云音乐]新碟上架"
    info = u"首页>发现音乐>新碟上架>全部新碟>全部，前45张；"
    name = "netease_web__new_album"
    allowed_domains = ["music.163.com"]
    first_css = 'div#nowplaying li[data-title]'
    second_css = '::attr(data-title)'
    count_limit = 45
    start_url = 'http://music.163.com/api/album/new?area=ALL&offset=0&total=true&limit=45&csrf_token='

    def start_requests(self):
        req = Request(url = self.start_url,
                      headers = {
                          'Accept-Language': ['en'], 
                          'Accept-Encoding': ['gzip,deflate'], 
                          'Accept': ['text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'], 
                          'User-Agent': ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36'],
                          'Referer': 'http://music.163.com/discover/album/'}
                      )
        return [req]
    
    def parse(self, response):
        try:
            info = json.loads(response.body)
            albums = info['albums']
        except Exception,e:
            err = self.name + ':' + str(e)
            raise CloseSpider(err)

        count = 0
        for album in albums:
            count += 1
            if count > self.count_limit:
                raise CloseSpider('done')
                
            item = KuwoScrapyItem()
            item['basic_source_info'] = '{}'
            item['basic_source_name'] = album['name']
            item['basic_source_artist'] = '&'.join([ar['name'] for ar in album['artists']])
            yield item


class NeteaseIndexNewAlbum(scrapy.Spider):
    desc = u"[网易云音乐首页]新碟上架"
    info = u"首页>发现音乐>推荐>新碟上架，前20张；"
    name = "netease_index__new_album"
    allowed_domains = ["music.163.com"]

    start_urls = (
        'http://music.163.com/discover',
    )

    filter_css = ''
    name_css = ''
    artist_css = ''
    count_limit = 20

    def parse(self, response):
        try:
            albums = response.css('#album-roller ul.f-cb li')
        except Exception,e:
            err = self.name + ':' + str(e)
            raise CloseSpider(err)

        count = 0
        for album in albums:
            count += 1
            if count > self.count_limit:
                raise CloseSpider('done')

            loader = ItemLoader(KuwoScrapyItem(), album)
            loader.add_value('basic_source_info', '{}')
            loader.add_css('basic_source_name', 'a[href^="/album?id="]::attr(title)', Join())
            loader.add_css('basic_source_artist','a[href^="/artist?id="]::attr(title)', Join())
            yield loader.load_item()
