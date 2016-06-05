# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from pymongo.collection import Collection
from pymongo.database import Database
import datetime

from lagou.items import PositionItem, JobDetailItem
from util import tools
# from data_model import DBSession, JobBrief

import config

class _BaseMongoPipeline(object):
    def __init__(self):
        self.client = tools.get_mongo_client()
        """:type: pymongo.MongoClient"""
        self.db = tools.get_lagou_db(self.client)
        """:type: Database"""
        self.collection_name = ''
        self.collection = None
        """:type: Collection"""


    def open_spider(self, spider):
        raise NotImplementedError()


class PositionPipeline(_BaseMongoPipeline):
    def open_spider(self, spider):
        self.collection = tools.get_job_brief_collection(self.db)

    def process_item(self, item, spider):
        """

        :param item:
        :param spider:
        :type data: PositionItem
        :return:
        """

        if not isinstance(item, PositionItem):
            return item

        data = dict(item)
        data['datetime'] = datetime.datetime.now()

        self.collection.insert_one(data)

        return item


class JobDetailPipeline(_BaseMongoPipeline):
    def open_spider(self, spider):
        self.collection = tools.get_job_detail_collection(self.db)

    def process_item(self, item, spider):
        if not isinstance(item, JobDetailItem):
            return item

        data = dict(item)
        data['datetime'] = datetime.datetime.now()

        self.collection.insert_one(data)

        return item
