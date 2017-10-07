# -*- coding: utf-8 -*-
import scrapy
import re

class SlotSpider(scrapy.Spider):
    name = 'slot'
    allowed_domains = ['slotcatalog.com']

    # This is the first index page.
    #
    start_urls = ['https://slotcatalog.com/en/type/Video_Slots']

    def parse(self, response):
        # Crawl horizontally (moving across index).
        #
        # This selector should really return only one element.
        #
        next_selector = response.css('li.next > a::attr(href)')
        #
        # Add it to the stack (URLs are treated with LIFO).
        #
        for url in next_selector.extract():
            yield scrapy.Request(response.urljoin(url))

        # Crawl vertically (visiting each of the games linked from index page).
        #
        item_selector = response.css('div.gameItemimg > a::attr(href)')

        for url in item_selector.extract():
            yield scrapy.Request(response.urljoin(url), callback=self.parse_item)

    def parse_item(self, response):
        name = response.css('div.divHead > h1::text').extract_first()
        #
        # Replace (Unicode version of) &nbsp;.
        #
        name = name.replace(u'\xa0', u' ')
        #
        name = re.search("Review of ([^(]*)", name).group(1).strip()

        rtp = response.css('div.slot_page_item_one > div:nth-child(4) > div > p > span::text').extract_first()
        #
        rtp = rtp.replace('%', '')

        provider = response.css("div.provider_item > p > span > a > span::text").extract_first()

        yield {
            'name': name,
            'rtp': rtp,
            'provider': provider,
        }
