# -*- coding: utf-8 -*-
import json
import math
import scrapy
import functools
from scrapy.http import Response
from scrapy.log import logger

from lagou.items import InterviewReviewItem

class CompanyInterviewReviewSpider(scrapy.Spider):
    name = "company_interview_review"
    allowed_domains = ["lagou.com"]
    start_urls = ( )

    interview_review_url_fmt = 'http://www.lagou.com/gongsi/interviewExperiences.html?companyId={company_id}'

    def start_requests(self):
        company_ids = [74507,]

        for company_id in company_ids:
            yield self._gen_form_req(
                company_id = company_id,
                callback = functools.partial(self.parse_initial_page, company_id=company_id),
                pagenum=1
            )

    def parse_initial_page(self, response, company_id):
        sel = response.xpath('//script[@id="interviewExperiencesData"]/text()')
        review_data = json.loads(sel.extract()[0])

        total_count = int(review_data['totalCount'])
        page_size = int(review_data['pageSize'])

        total_page = math.ceil(total_count / page_size)
        for pagenum in range(0, total_page):
            yield self._gen_form_req(
                company_id=company_id,
                callback=self.parse_page,
                pagenum=pagenum,
                page_size=page_size
            )

    def parse_page(self, response):
        """

        :param response:
        :type response: Response
        :return:
        """

        sel = response.xpath('//script[@id="interviewExperiencesData"]/text()')
        review_data = json.loads(sel.extract()[0])
        item = InterviewReviewItem()

        result = review_data['result']
        for each in result:
            item['company_id'] = each['companyId']
            item['company_name'] = each['companyName']

            item['position_id'] = each['positionId']
            item['position_name'] = each['positionName']
            item['position_status'] = each.get('positionStatus', 1)

            item['review_content_list'] = []
            item['review_date'] = each['createTime']
            item['review_person_name'] = each['username']
            item['review_reply'] = each.get('reply', {})
            item['review_reply_count'] = each['replyCount']
            item['review_tags'] = each['tagArray']
            item['review_useful_count'] = each['usefulCount']

            item['score_company'] = each['companyScore']
            item['score_comprehensive'] = each['comprehensiveScore']
            item['score_describe'] = each['describeScore']
            item['score_interviewer'] = each['interviewerScore']
            item['score_my'] = each['myScore']

            yield item

    def _gen_form_req(self, company_id, callback, pagenum, page_size=10):

        return scrapy.FormRequest(
            self.interview_review_url_fmt.format(company_id=company_id),
            formdata={
                'companyId': str(company_id),
                'pageSize': str(page_size),
                'pageNo': str(pagenum),
            },
            callback=callback,
            method='POST'
        )

    def _company_id_iter(self):
        return iter([])