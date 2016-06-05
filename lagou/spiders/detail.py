# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.http import Response
from bs4 import BeautifulSoup

from lagou.items import JobDetailItem

class DetailSpider(scrapy.Spider):
    name = "detail"
    allowed_domains = ["lagou.com"]
    start_urls = (
        'http://www.lagou.com/',
    )

    job_url_fmt = 'http://www.lagou.com/jobs/{job_id}.html'
    job_ids = []

    def start_requests(self):
        for job_id in self.job_ids:
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