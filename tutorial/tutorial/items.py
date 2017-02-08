# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DmozItem(scrapy.Item):
	#小说名
    title = scrapy.Field()
    #最新章节
    new_page = scrapy.Field()
    #内容
    desc = scrapy.Field()
    #链接
    link = scrapy.Field()
