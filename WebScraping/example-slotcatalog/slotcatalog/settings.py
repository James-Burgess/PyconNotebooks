# -*- coding: utf-8 -*-

BOT_NAME = 'slotcatalog'

SPIDER_MODULES = ['slotcatalog.spiders']
NEWSPIDER_MODULE = 'slotcatalog.spiders'

ROBOTSTXT_OBEY = True

CONCURRENT_REQUESTS = 2

FEED_FORMAT = "json"
FEED_URI = "slots.json"
