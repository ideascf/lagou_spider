# -*- coding: utf-8 -*-
import json
import math
import scrapy
import functools
from scrapy.log import logger
from scrapy.http import Response

from lagou.items import PositionItem
import config

class PositionSpider(scrapy.Spider):
    name = "position"
    allowed_domains = ["lagou.com"]
    start_urls = (
        'http://www.lagou.com/',
    )

    position_url = 'http://www.lagou.com/jobs/positionAjax.json?'

    def start_requests(self):
        for kw in config.LAGOU_KEYWORDS:
            yield self._gen_form_req(1, kw, callback=functools.partial(self.parse_initial_page, keyword=kw))

    def parse_initial_page(self, response, keyword):
        logger.debug(response.body)

        job_data = json.loads(response.body.decode('utf8'))
        job_content = job_data['content']
        job_position_result = job_content['positionResult']

        total_page_num = math.ceil(job_position_result['totalCount'] / config.LAGOU_JOB_PER_PAGE)
        for pagenum in range(1, total_page_num):
            yield self._gen_form_req(pagenum, keyword, callback=functools.partial(self.parse_page, keyword=keyword))

    def parse_page(self, response, keyword):
        """

        :param response:
        :type response: Response
        :return:
        """

        logger.debug(response.body)

        item = PositionItem()
        job_data = json.loads(response.body.decode('utf8'))
        job_content = job_data['content']
        job_position_result = job_content['positionResult']
        job_result = job_position_result['result']

        for each in job_result:
            item['company_id'] = each['companyId']
            item['company_name'] = each['companyName']
            item['company_size'] = each['companySize']
            item['company_label_list'] = each['companyLabelList']
            item['company_logo'] = each['companyLogo']

            salary = each['salary']
            salary = salary.split('-')
            if len(salary) == 1:  # 固定工资
                item['salary_max'] = self._float_salary(salary[0])
            else:  # 范围工资
                item['salary_max'] = self._float_salary(salary[1])
            item['salary_min'] = self._float_salary(salary[0])
            item['salary_avg'] = (item['salary_max'] + item['salary_min']) / 2
            item['position_id'] = each['positionId']
            item['position_name'] = each['positionName']
            item['position_first_type'] = each['positionFirstType']
            item['position_type'] = each['positionType']
            item['position_advantage'] = each['positionAdvantage']

            item['work_year'] = each['workYear']
            item['education'] = each['education']
            item['job_nature'] = each['jobNature']

            item['city'] = each['city']
            item['keyword'] = keyword
            item['industry_field'] = each['industryField']
            item['district'] = each['district']
            item['finance_stage'] = each['financeStage']
            item['leader'] = each['leaderName']
            item['job_create_time'] = each['createTime']



            yield item


    def _float_salary(self, salary):
        """

        :param salary:
        :type salary: str
        :return:
        :rtype: float
        """

        k_pos = salary.find('k')
        return float(salary[:k_pos])

    def _gen_form_req(self, pagenum, keyword, callback=None):
        if callback is None:
            callback = self.parse

        return scrapy.FormRequest(
            self.position_url,
            formdata={
                'pn': str(pagenum),
                'kd': keyword,
            },
            callback=callback
        )
