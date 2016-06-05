# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from pymongo.collection import Collection
from pymongo.database import Database
import datetime

from lagou.items import LagouItem
# from data_model import DBSession, JobBrief
from scrapy.conf import settings

class _BaseMongoPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_NAME']

        self.client = pymongo.MongoClient(host, port)
        """:type: pymongo.MongoClient"""
        self.db = self.client[dbname]
        """:type: Database"""
        self.collection_name = ''
        self.collection = None
        """:type: Collection"""


    def open_spider(self, spider):
        raise NotImplementedError()


class LagouPipeline(_BaseMongoPipeline):
    def __init__(self):
        super(LagouPipeline, self).__init__()

        self.collection_name = settings['MONGODB_COLLECTION_BRIEF']

    def open_spider(self, spider):
        self.collection = self.db[self.collection_name]

    def process_item(self, item, spider):
        """

        :param item:
        :param spider:
        :type data: LagouItem
        :return:
        """

        data = dict(item)
        data['datetime'] = datetime.datetime.now()

        self.collection.insert_one(data)

        return item


class JobDetailPipeline(_BaseMongoPipeline):
    def __init__(self):
        super(JobDetailPipeline, self).__init__()

        self.collection_name = settings['MONGODB_COLLECTION_DETAIL']

    def open_spider(self, spider):
        self.collection = self.db[self.collection_name]

    def process_item(self, item, spider):

        data = dict(item)
        data['datetime'] = datetime.datetime.now()

        self.collection.insert_one(data)

        return item
