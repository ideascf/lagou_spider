# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

from lagou.items import LagouItem
from data_model import DBSession, JobBrief


class _BaseSqlitePipeline(object):
    def __init__(self):
        self.client = None
        self.db_name = ''

    def open_spider(self, spider):
        self.client = sqlite3.connect('./data.db')

class LagouPipeline(_BaseSqlitePipeline):

    def open_spider(self, spider):
        super().open_spider(spider)

        self.client.execute(
            '''
            CREATE TABLE IF NOT EXISTS job_brief
            (
              `id` INTEGER PRIMARY KEY AUTOINCREMENT,
              city VARCHAR (256),
              keyword VARCHAR (256),
              company_name VARCHAR (256),
              company_size VARCHAR (256),
              company_label_list VARCHAR (256),

              salary_min FLOAT (10, 2),
              salary_max FLOAT (10, 2),
              salary_avg FLOAT (10, 2),

              position_name VARCHAR (256),
              position_type VARCHAR (256),
              position_advantage VARCHAR (256)
            )
            '''
        )

    def process_item(self, item, spider):
        """

        :param item:
        :param spider:
        :type item: LagouItem
        :return:
        """
        item = dict(item)

        job_brief = JobBrief()
        for key,value in item.items():
            setattr(job_brief, key, str(value))

        session = DBSession()
        session.add(job_brief)
        session.commit()
        session.close()

        return item

class JobDetailPipeline(object):
    def process_item(self, item, spider):
        return item
