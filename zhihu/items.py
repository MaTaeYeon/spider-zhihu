# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ArticleItem(scrapy.Item):
    nickname = scrapy.Field()
    avatar = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    cover = scrapy.Field()
    img_list = scrapy.Field()
    content_str = scrapy.Field()
    tag_str = scrapy.Field()
    publish_date = scrapy.Field()
    url = scrapy.Field()
