# -*- coding: utf-8 -*-
from testscrapy import settings
import pymongo

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TestscrapyPipeline(object):

    def __init__(self):
        host = settings.mongodb_host
        port = settings.mongodb_port
        dbname = settings.mongodb_db_name
        collection = settings.mongodb_db_collection

        client = pymongo.MongoClient(host=host, port=port)
        self.post = client[dbname][collection]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
