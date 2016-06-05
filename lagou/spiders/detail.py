# -*- coding: utf-8 -*-
import re
import scrapy
import pymongo
from scrapy.http import Response
from bs4 import BeautifulSoup

from lagou.items import JobDetailItem
from util import tools

class DetailSpider(scrapy.Spider):
    name = "detail"
    allowed_domains = ["lagou.com"]
    start_urls = (
        'http://www.lagou.com/',
    )

    job_url_fmt = 'http://www.lagou.com/jobs/{job_id}.html'

    def start_requests(self):
        client = tools.get_mongo_client()
        db = tools.get_lagou_db(client)
        brief_collection = tools.get_job_brief_collection(db)

        result = brief_collection.find({}, {'position_id':1, '_id': 0})
        position_ids = (each['position_id'] for each in result)

        for job_id in position_ids:
            yield self._gen_form_req(job_id)

    def parse(self, response):
        """

        :param response:
        :type response: Response
        :return:
        """

        item = JobDetailItem()
        html = response.body
        job_id = re.match(r'http://www\.lagou\.com/jobs/(\d+)\.html', response.url).groups()[0]
        soup = BeautifulSoup(html, 'html.parser')

        job_bt_soup = soup.find('dd', class_='job_bt')
        if job_bt_soup is not None:
            job_bt = job_bt_soup.text

            item['job_id'] = job_id
            item['job_bt'] = job_bt

            yield item

    def _gen_form_req(self, job_id):
        return scrapy.FormRequest(
            url=self.job_url_fmt.format(job_id=job_id)
        )