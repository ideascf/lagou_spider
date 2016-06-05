# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PositionItem(scrapy.Item):
    # 公司
    company_id = scrapy.Field()  # 公司ID
    company_name = scrapy.Field()  # 公司名称
    company_size = scrapy.Field()  # 公司规模
    company_label_list = scrapy.Field()  # 公司标签
    company_logo = scrapy.Field()  # 公司logo

    # 薪资
    salary_max = scrapy.Field()
    salary_min = scrapy.Field()
    salary_avg = scrapy.Field()

    # 职位
    position_id = scrapy.Field()  # 职位ID
    position_name = scrapy.Field()  # 职位名称
    position_first_type = scrapy.Field()  # 职位所属大分类
    position_type = scrapy.Field()  # 职位类型
    position_advantage = scrapy.Field()  # 职位优势

    # 限制条件
    work_year = scrapy.Field()  # 工作年限
    education = scrapy.Field()  # 学历要求
    job_nature = scrapy.Field()  # 兼职/全职

    # 其它
    city = scrapy.Field()  # 所在城市
    keyword = scrapy.Field()  # 搜索关键字
    industry_field = scrapy.Field()  # 行业分类
    district = scrapy.Field()  # 工作地点所属区域
    finance_stage = scrapy.Field()  # 发展阶段
    leader = scrapy.Field()  # 公司领导人
    job_create_time = scrapy.Field()  # 职位发布时间
    

class JobDetailItem(scrapy.Item):
    job_id = scrapy.Field()
    job_bt = scrapy.Field()
