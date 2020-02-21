# -*- coding: utf-8 -*-
import scrapy


class DaguSpider(scrapy.Spider):
    name = 'dagu'
    allowed_domains = ['http://www.fl5y.com/xiazai/dagushu/index.html']
    start_urls = ['http://http://www.fl5y.com/xiazai/dagushu/index.html/']

    def parse(self, response):
        pass
