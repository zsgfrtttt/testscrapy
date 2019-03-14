# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    img = scrapy.Field()
    name = scrapy.Field()
    score = scrapy.Field()
    pass


#http://59.37.131.27:8084/appServer/app/home/getUrl?channel=xedApp&packageName=com.xedfun.android.app&reqApplicationType=XED&mobileId=aaf95f30&versionCode=5&token=&userId=&mobile=&channelCode=xedApp&versionName=v1.3.1&appDownChannel=umeng&mobileModel=MI4LTE&productCode=XED&osName=Android&osVersion=6.0.1&reqApplicationVersion=5&tokenUserId=