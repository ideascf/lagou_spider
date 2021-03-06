# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PositionItem(scrapy.Item):
    """
    职位简介
    """

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
    """
    职位详情
    """

    job_id = scrapy.Field()
    job_bt = scrapy.Field()


class CompanyItem(scrapy.Item):
    """
    公司
    """

    # 公司相关数据
    position_num = scrapy.Field()  # 招聘职位数量
    resume_deal_timely_rate = scrapy.Field()  # 简历及时处理率
    resume_deal_cost_time = scrapy.Field()  # 简历处理平均耗时
    interview_comment_num = scrapy.Field()  # 面试评价数量
    last_login_time = scrapy.Field()  # 企业职位管理者上次登陆时间

    # 产品介绍
    product_list = scrapy.Field()  # product_name,  product_url,  product_intro

    # 公司
    company_tags = scrapy.Field()  # 公司标签
    company_intro = scrapy.Field()  # 公司简介
    compayn_history_list = scrapy.Field()  # 公司发展历程

    # 面试评价
    review_list = scrapy.Field()  # 面试评价list


class InterviewReviewItem(scrapy.Item):
    """
    面试评价
    """


    company_id = scrapy.Field()  # 公司ID
    company_name = scrapy.Field()  # 公司名称

    position_id = scrapy.Field()  # 职位ID
    position_name = scrapy.Field()  # 面试职位
    position_status = scrapy.Field()  # 职位状态

    review_tags = scrapy.Field()  # 评价标签
    review_content_list = scrapy.Field()  # 评价内容列表  review_type,  review_body
    review_useful_count = scrapy.Field()  # '有用'数
    review_reply = scrapy.Field()  # 评价回复(职位管理人的回复)
    review_reply_count = scrapy.Field()  # 评价回复总数
    review_person_name = scrapy.Field()  # 评价人
    review_date = scrapy.Field()  # 评价日期

    score_describe = scrapy.Field()  #  描述相符分数
    score_interviewer = scrapy.Field()  # 面试官分数
    score_company = scrapy.Field()  # 公司分数
    score_comprehensive = scrapy.Field()  # 综合分数
    score_my = scrapy.Field()