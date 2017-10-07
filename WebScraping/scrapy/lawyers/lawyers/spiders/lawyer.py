# -*- coding: utf-8 -*-
import scrapy, string


class LawyerSpider(scrapy.Spider):
    name = 'lawyer'
    allowed_domains = ['www.webberwentzel.com/']
    # start_urls = ['http://www.webberwentzel.com//']

    def start_requests(self):   
    	url_base = 'http://www.webberwentzel.com/wwb/content/en/ww/ww-our-people?as_request=as_results&character='

    	for letter in string.ascii_uppercase[0]:
    		yield scrapy.Request(url_base+letter)

    def parse(self, response):
        for url in response.css('a[href^=ww-people-profile]::attr(href)').extract():
        	yield scrapy.Request(response.urljoin(url))
        
        name = response.css('.profile_name::text').extract()
        email = reponse.css('a[href^=mailto:]::text').extract()
        

       if name:
       		yield{
       			name:'name',
       			email:'email'
       		}

