# -*- coding: utf-8 -*-
import json
import funcs
import scrapy

from kuwo_scrapy.items import KuwoScrapyItem
from kuwo_scrapy.pipelines import KuwoScrapyDBConnector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst
from scrapy.exceptions import *


class QqPcNewAlbumSpider(scrapy.Spider):
    desc = u"[QQ客户端首页]专辑首发"
    info = u"qq客户端首页>专辑首发，5张专辑"
    name = "qq_pc__new_album"
    allowed_domains = ["music.qq.com"]
    start_urls = (
        'http://music.qq.com/json/first/index_sub.json',
    )
    deep_key = 'al.new'
    count = 5

    def parse(self, response):
        try:
            info = json.loads(response.body)
            news = funcs.deep(info, self.deep_key)
        except Exception,e:
            err = self.name + ':' + str(e)
            raise CloseSpider(err)

        count = 0
        for new in news:
            count += 1
            if count > self.count:
                raise CloseSpider('done')
                
            item = KuwoScrapyItem()
            item['basic_source_info'] = '{}'
            item['basic_source_name'] = new['Falbum_name']
            item['basic_source_artist'] = new['Fsinger_name']

            yield item


class QqPcRecmAlbumNdSpider(scrapy.Spider):
    desc = u"[QQ客户端]内地专辑"
    info = u"qq客户端首页>专辑首发(更多)>推荐专辑>内地，前5张专辑"
    name = "qq_pc__recm_album_nd"
    allowed_domains = ["music.qq.com"]
    start_urls = (
        'http://music.qq.com/json/first/album/nd/20/1.json',
    )

    count = 5

    def parse(self, response):
        try:
            info = json.loads(response.body)
            recms = info['data']
        except Exception,e:
            err = self.name + ':' + str(e)
            raise CloseSpider(err)

        count = 0
        for recm in recms:
            count += 1
            if count > self.count:
                raise CloseSpider('done')

            item = KuwoScrapyItem()
            item['basic_source_info'] = '{}'
            item['basic_source_name'] = recm['Falbum_name']
            item['basic_source_artist'] = recm['Fsinger_name']
            yield item


class QqPcRecmAlbumGtSpider(QqPcRecmAlbumNdSpider):
    desc = u"[QQ客户端]港台专辑"
    info = u"qq客户端首页>专辑首发(更多)>推荐专辑>港台，前5张专辑"
    name = "qq_pc__recm_album_gt"
    allowed_domains = ["music.qq.com"]
    start_urls = (
        'http://music.qq.com/json/first/album/gt/20/1.json',
    )



class QqPcRecmAlbumEuSpider(QqPcRecmAlbumNdSpider):
    desc = u"[QQ客户端]欧美专辑"
    info = u"qq客户端首页>专辑首发(更多)>推荐专辑>欧美，前5张专辑"
    name = "qq_pc__recm_album_eu"
    allowed_domains = ["music.qq.com"]
    start_urls = (
        'http://music.qq.com/json/first/album/eu/20/1.json',
    )



class QqPcRecmAlbumKrSpider(QqPcRecmAlbumNdSpider):
    desc = u"[QQ客户端]韩语专辑"
    info = u"qq客户端首页>专辑首发(更多)>推荐专辑>韩语，前5张专辑"
    name = "qq_pc__recm_album_kr"
    allowed_domains = ["music.qq.com"]
    start_urls = (
        'http://music.qq.com/json/first/album/k/20/1.json',
    )


class QqPcRecmAlbumJpSpider(QqPcRecmAlbumNdSpider):
    desc = u"[QQ客户端]日语专辑"
    info = u"qq客户端首页>专辑首发(更多)>推荐专辑>日语，前5张专辑"
    name = "qq_pc__recm_album_jp"
    allowed_domains = ["music.qq.com"]
    start_urls = (
        'http://music.qq.com/json/first/album/j/20/1.json',
    )


class QqPcSingleNdSpider(scrapy.Spider):
    desc = u"[QQ客户端首页]内地单曲"
    info = u"qq客户端首页>首发>内地>单曲，前32首歌曲"
    name = "qq_pc__single_nd"
    allowed_domains = ["music.qq.com"]
    start_urls = (
        'http://music.qq.com/json/first/index_sub.json',
    )
    deep_key = 'sl.nd'

    count = 32


    def parse(self, response):
        try:
            info = json.loads(response.body)
            news = funcs.deep(info, self.deep_key)
        except Exception,e:
            err = self.name + ':' + str(e)
            raise CloseSpider(err)

        count = 0
        for new in news:
            count += 1
            if count > self.count:
                raise CloseSpider('done')

            item = KuwoScrapyItem()    
            datas = new['data'].split('|')
            item['basic_source_info'] = '{}'
            item['basic_source_name'] = datas[1] 
            item['basic_source_artist'] = datas[3]

            yield item


class QqPcSingleEuSpider(QqPcSingleNdSpider):
    desc = u"[QQ客户端首页]欧美单曲"
    info = u"qq客户端首页>首发>欧美>单曲，前32首歌曲"
    name = "qq_pc__single_eu"
    allowed_domains = ["music.qq.com"]
    start_urls = (
        'http://music.qq.com/json/first/index_sub.json',
    )
    deep_key = 'sl.eu'


class QqPcSingleGtSpider(QqPcSingleNdSpider):
    desc = u"[QQ客户端首页]港台单曲"
    info = u"qq客户端首页>首发>港台>单曲，前32首歌曲"
    name = "qq_pc__single_gt"
    allowed_domains = ["music.qq.com"]
    start_urls = (
        'http://music.qq.com/json/first/index_sub.json',
    )
    deep_key = 'sl.gt'


class QqPcSingleKrSpider(QqPcSingleNdSpider):
    desc = u"[QQ客户端首页]韩语单曲"
    info = u"qq客户端首页>首发>韩语>单曲，前32首歌曲"
    name = "qq_pc__single_kr"
    allowed_domains = ["music.qq.com"]
    start_urls = (
        'http://music.qq.com/json/first/index_sub.json',
    )
    deep_key = 'sl.k'


class QqPcSingleJpSpider(QqPcSingleNdSpider):
    desc = u"[QQ客户端首页]日语单曲"
    info = u"qq客户端首页>首发>日语>单曲，前32首歌曲"
    name = "qq_pc__single_jp"
    allowed_domains = ["music.qq.com"]
    start_urls = (
        'http://music.qq.com/json/first/index_sub.json',
    )
    deep_key = 'sl.j'


class QqPcQualityUpMovieSpider(scrapy.Spider):
    desc = u"[QQ客户端_音质提升]影视热歌"
    info = u"首页>热门分类(更多)>热门>影视热歌,前120首歌曲音质变更提醒；"
    name = "qq_pc__quality_up_movie"
    allowed_domains = ["music.qq.com"]
    start_urls = (
        'http://music.qq.com/json/category/song/16_1_listen_0/120/1.json',
    )
    deep_key = 'data.list'
    count_limit = 120

    def parse(self, response):
        try:
            info = json.loads(response.body)
            news = funcs.deep(info, self.deep_key)
        except Exception,e:
            err = self.name + ':' + str(e)
            raise CloseSpider(err)

        count = 0
        for new in news:
            count += 1
            if count > self.count_limit:
                raise CloseSpider('done')
                
            music_data = new['musicData'].split("|")
            quality = {"HQ": long(music_data[17]) > 0 or long(music_data[18]) > 0 , "SQ": long(music_data[15]) > 0 or long(music_data[16]) > 0 }
            #quality = {"HQ1": music_data[17], "HQ2": music_data[18], "SQ1": music_data[15], "SQ2": music_data[16]}
            item = KuwoScrapyItem()
            item['basic_source_info'] = json.dumps(quality, ensure_ascii = False)
            item['basic_source_name'] = music_data[1]
            item['basic_source_artist'] = music_data[3]
            yield item


class QqPcQualityUpClassicSpider(QqPcQualityUpMovieSpider):
    desc = u"[QQ客户端_音质提升]经典好歌"
    info = u"首页>热门分类(更多)>热门>经典好歌,前120首歌曲音质变更提醒；"
    name = "qq_pc__quality_up_jd"
    allowed_domains = ["music.qq.com"]
    start_urls = (
        'http://music.qq.com/json/category/song/1841_1_listen_0/120/1.json',
    )
    deep_key = 'data.list'
    count_limit = 120


class QqPcQualityUpDJSpider(QqPcQualityUpMovieSpider):
    desc = u"[QQ客户端_音质提升]DJ舞曲"
    info = u"首页>热门分类(更多)>热门>DJ舞曲，前120首歌曲音质变更提醒；"
    name = "qq_pc__quality_up_dj"
    allowed_domains = ["music.qq.com"]
    start_urls = (
        'http://music.qq.com/json/category/song/1841_1_listen_0/120/1.json',
    )
    deep_key = 'data.list'
    count_limit = 120


class QqPcQualityUpKaraSpider(QqPcQualityUpMovieSpider):
    desc = u"[QQ客户端_音质提升]K歌金榜"
    info = u"首页>热门分类(更多)>热门>K歌金榜，前120首歌曲音质变更提醒；"
    name = "qq_pc__quality_up_kara"
    allowed_domains = ["music.qq.com"]
    start_urls = (
        'http://music.qq.com/json/category/song/2160_1_listen_0/120/1.json',
    )
    deep_key = 'data.list'
    count_limit = 120


class QqPcQualityUpPopSpider(QqPcQualityUpMovieSpider):
    desc = u"[QQ客户端_音质提升]流行热歌"
    info = u"首页>热门分类(更多)>热门>流行热歌，前120首歌曲音质变更提醒；"
    name = "qq_pc__quality_up_pop"
    allowed_domains = ["music.qq.com"]
    start_urls = (
        'http://music.qq.com/json/category/song/309_4_listen_0/120/1.json',
    )
    deep_key = 'data.list'
    count_limit = 120


class QqPcQualityUpClassicalSpider(QqPcQualityUpMovieSpider):
    desc = u"[QQ客户端_音质提升]古典"
    info = u"首页>热门分类(更多)>热门>古典，前120首歌曲音质变更提醒；"
    name = "qq_pc__quality_up_classical"
    allowed_domains = ["music.qq.com"]
    start_urls = (
        'http://music.qq.com/json/category/song/2164_1_listen_0/120/1.json',
    )
    deep_key = 'data.list'
    count_limit = 120
