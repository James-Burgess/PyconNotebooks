# -*- coding: utf-8 -*-
import scrapy

class QuoteSpider(scrapy.Spider):
    # The name identifies this spider. Each spider in a project should have a
    # unique name.
    #
    name = 'Quote'

    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # Extract page content.
        #
        # Using css() to access Selectors but can also use xpath().
        #
        # Beautiful Soup another option for parsing the page.
        #
        for quote in response.css("div.quote"):
            yield {
                'text': quote.css("span.text::text").extract_first(),
                'author': quote.css("small.author::text").extract_first(),
                'tags': quote.css("div.tags > a.tag::text").extract()
            }

        # Find new URLs.
        #
        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))




