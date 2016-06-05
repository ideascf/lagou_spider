# -*- coding: utf-8 -*-
import json
import math
import scrapy
from scrapy.log import logger
from scrapy.http import Response

from lagou.items import LagouItem

class PositionSpider(scrapy.Spider):
    name = "position"
    allowed_domains = ["lagou.com"]
    start_urls = (
        'http://www.lagou.com/',
    )

    position_url = 'http://www.lagou.com/jobs/positionAjax.json?'
    curpage = 1
    keywords = ['go', 'python', '后端']
    curkw_index = 0
    keyword = keywords[0]
    total_page_num = 0
    JOB_PER_PAGE = 15

    def start_requests(self):
        yield self._gen_form_req()

    def parse(self, response):
        """

        :param response:
        :type response: Response
        :return:
        """

        logger.debug(response.body)

        item = LagouItem()
        job_data = json.loads(response.body.decode('utf8'))
        job_content = job_data['content']
        job_position_result = job_content['positionResult']
        job_result = job_position_result['result']

        self.total_page_num = math.ceil(job_position_result['totalCount'] / self.JOB_PER_PAGE)
        for each in job_result:
            item['city'] = each['city']
            item['keyword'] = self.keyword

            item['company_size'] = each['companySize']
            item['company_name'] = each['companyName']
            item['company_label_list'] = each['companyLabelList']

            item['position_name'] = each['positionName']
            item['position_type'] = each['positionType']
            item['position_advantage'] = each['positionAdvantage']

            salary = each['salary']
            salary = salary.split('-')
            if len(salary) == 1:  # 固定工资
                item['salary_max'] = self._float_salary(salary[0])
            else:  # 范围工资
                item['salary_max'] = self._float_salary(salary[1])
            item['salary_min'] = self._float_salary(salary[0])
            item['salary_avg'] = (item['salary_max'] + item['salary_min']) / 2

            yield item

        # check next
        if self.curpage < self.total_page_num:
            self.curpage += 1
            yield self._gen_form_req()
        elif self.curkw_index < len(self.keywords)-1:  # 另外的分类
            self.curpage = 1  # reset page
            self.total_page_num = 0
            self.curkw_index += 1  # next kd
            self.keyword = self.keywords[self.curkw_index]

            yield self._gen_form_req()


    def _float_salary(self, salary):
        """

        :param salary:
        :type salary: str
        :return:
        :rtype: float
        """

        k_pos = salary.find('k')
        return float(salary[:k_pos])

    def _gen_form_req(self, callback=None):
        if callback is None:
            callback = self.parse

        return scrapy.FormRequest(
            self.position_url,
            formdata={
                'pn': str(self.curpage),
                'kd': self.keyword,
            },
            callback=callback
        )
