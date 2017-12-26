# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    CATEGORY = scrapy.Field()
    SUBCATEGORY = scrapy.Field()
    WEBSITE = scrapy.Field()
    DESCRIPTION = scrapy.Field()
    DISCOUNT = scrapy.Field()
    OLD_PRICE = scrapy.Field()
    NEW_PRICE = scrapy.Field()
    PDP_URL = scrapy.Field()


