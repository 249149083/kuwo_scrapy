# -*- coding: utf-8 -*-
import time
import funcs
import scrapy
import datetime
import calendar

from kuwo_scrapy.items import KuwoScrapyItem
from kuwo_scrapy.pipelines import KuwoScrapyDBConnector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst
from scrapy.exceptions import *

class BillBoardSpider(scrapy.Spider):
    desc = u"[美国billboard榜]"
    info = u"榜单top100首"
    name = "billboard__music"
    allowed_domains = ["www.billboard.com"]
    start_urls = (
        'http://www.billboard.com/charts/hot-100',
    )

    filter_css = 'article[id^="row"] div.row-title'
    name_css = 'h2::text'
    artist_css = 'h3 a::text'
    
    count_limit = 100

    
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


class MnetDailySpider(BillBoardSpider):
    desc = u"[韩国M-net榜]天榜"
    info = u"每天榜单top100首；"
    name = "mnet__music_daily"
    allowed_domains = ["www.mnet.com"]
    time_str = time.strftime('%Y%m%d%H')
    start_urls = (
        'http://www.mnet.com/chart/TOP100/%s?pNum=1' % time_str,
        'http://www.mnet.com/chart/TOP100/%s?pNum=2' % time_str,
    )

    filter_css = 'div.MMLTable td.MMLItemTitle div.MMLITitle_Box'
    name_css = 'a.MMLI_Song::attr(title)'
    artist_css = 'a.MMLIInfo_Artist::text'
    
    count_limit = 102 # 有两首是推荐歌曲,包含在100之中,不过要遍历


last_sunday = funcs.delay_weekday(weekday = calendar.SUNDAY, forward = False)

class MnetWeeklySpider(BillBoardSpider):
    desc = u"[韩国M-net榜]周榜"
    info = u"每周榜单top100首；"
    name = "mnet__music_weekly"
    allowed_domains = ["www.mnet.com"]
    time_str = funcs.delay_weekday(start_day = last_sunday, weekday = calendar.MONDAY, forward = False).strftime('%Y%m%d') + '-' + last_sunday.strftime('%Y%m%d')
    start_urls = (
        'http://www.mnet.com/chart/TOP100/%s?pNum=1' % time_str,
        'http://www.mnet.com/chart/TOP100/%s?pNum=2' % time_str,
    )

    filter_css = 'div.MMLTable td.MMLItemTitle div.MMLITitle_Box'
    name_css = 'a.MMLI_Song::attr(title)'
    artist_css = 'a.MMLIInfo_Artist::text'
    
    count_limit = 102 # 有两首是推荐歌曲,包含在100之中,不过要遍历


class ItunesSpider(BillBoardSpider):
    desc = u"[itunes榜]"
    info = u"itunes榜100首；"
    name = "itunes__music"
    allowed_domains = ["www.apple.com"]
    start_urls = (
        'http://www.apple.com/itunes/charts/songs/',
    )

    filter_css = 'div#main section div.section-content li'
    name_css = 'h3 a::text'
    artist_css = 'h4 a::text'
    
    count_limit = 100 


two_days_ago = datetime.datetime.today() - datetime.timedelta(days = 2)

class OriconDailySpider(BillBoardSpider):
    desc = u"[日本Oricon榜]天榜"
    info = u"日本Oricon榜每天榜单歌曲30首"
    name = "oricon__music_daily"
    allowed_domains = ["www.oricon.com"]
    time_str = two_days_ago.strftime('%Y-%m-%d')
    start_urls = (
        'http://www.oricon.co.jp/rank/js/d/%s/' % (time_str),
        'http://www.oricon.co.jp/rank/js/d/%s/p/2/' % (time_str),
        'http://www.oricon.co.jp/rank/js/d/%s/p/3/' % (time_str),
    )

    filter_css = 'div#content-main div.content-rank-main section div.wrap-text'
    name_css = '.title::text'
    artist_css = '.name::text'
    
    count_limit = 30


class OriconWeeklySpider(BillBoardSpider):
    desc = u"[日本Oricon榜]周榜"
    info = u"日本Oricon榜每周榜单歌曲50首"
    name = "oricon__music_weekly"
    allowed_domains = ["www.oricon.com"]
    time_str = funcs.delay_weekday(weekday = calendar.MONDAY, forward = False).strftime('%Y-%m-%d')
    start_urls = (
        'http://www.oricon.co.jp/rank/js/w/%s/' % (time_str),
        'http://www.oricon.co.jp/rank/js/w/%s/p/2/' % (time_str),
        'http://www.oricon.co.jp/rank/js/w/%s/p/3/' % (time_str),
        'http://www.oricon.co.jp/rank/js/w/%s/p/4/' % (time_str),
        'http://www.oricon.co.jp/rank/js/w/%s/p/5/' % (time_str),
    )

    filter_css = 'div#content-main div.content-rank-main section div.wrap-text'
    name_css = '.title::text'
    artist_css = '.name::text'
    
    count_limit = 50


class ColashareSpider(BillBoardSpider):
    desc = u"新鲜志"
    info = u"新鲜志网站涉及歌曲、专辑"
    name = "colashare"
    allowed_domains = ["t.colashare.com"]
    start_urls = (
        'http://t.colashare.com/',
    )

    filter_css = 'div[id^="post"] h2'
    name_css = 'a::text'
    artist_css = 'none'
    
    count_limit = 999

