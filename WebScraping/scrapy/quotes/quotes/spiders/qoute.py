# -*- coding: utf-8 -*-
import scrapy


class QouteSpider(scrapy.Spider):
    name = 'qoute'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        pass
