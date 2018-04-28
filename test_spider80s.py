__author__ = "vcancy"

from unittest import TestCase

from scripts.spider80s import Spider80s


# /usr/bin/python
# -*-coding:utf-8-*-
class TestSpider80s(TestCase):
    def test__search_item(self):
        self.fail('1111')


class TestSpider80s(TestCase):
    def setUp(self):
        self.spider = Spider80s()

    def test__parse_page(self):
        self.spider._parse_page('16713')


class TestSpider80s(TestCase):
    def setUp(self):
        self.spider = Spider80s()

    def test__parse_search_list(self):
        data = {'keyword':'远大前程'}
        response = self.spider._request.request('POST',f'{self.spider.url}/search',data=data)
        self.spider._parse_search_list(response.text,'远大前程')