# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # 其它
    city = scrapy.Field()
    keyword = scrapy.Field()

    # 公司
    company_name = scrapy.Field()
    company_size = scrapy.Field()
    company_label_list = scrapy.Field()

    # 薪资
    salary_max = scrapy.Field()
    salary_min = scrapy.Field()
    salary_avg = scrapy.Field()

    # 职位
    position_name = scrapy.Field()
    position_type = scrapy.Field()
    position_advantage = scrapy.Field()


class JobDetailItem(scrapy.Item):
    job_id = scrapy.Field()
    job_bt = scrapy.Field()
