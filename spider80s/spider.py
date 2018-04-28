__author__ = "vcancy"
# /usr/bin/python
# -*-coding:utf-8-*-

"""
80s电影爬虫，爬取给定电影/电视剧的迅雷下载地址，输出到对应文件
"""

import sys
import logging
import re
import requests
from bs4 import BeautifulSoup

MOVIES = []

_LOG = logging.getLogger(__name__)
_LOG.setLevel(logging.INFO)
CH = logging.StreamHandler()
CH.setLevel(logging.INFO)
_LOG.addHandler(CH)


class Movie:
    """
    电影/电视剧抽象类
    """

    def __init__(self) -> None:
        self.id = None
        self.name = None
        self.type = None
        self.year = None
        self.rank = None
        self.downloads = None

    def get_urls(self):
        return ['{}[{}][{}]:\n{}\n'.format(download.name, download.type, download.size, download.address) for download in
                self.downloads]


class MovieDownload:
    """
    电影/电视剧下载信息
    """

    def __init__(self) -> None:
        self.name = None
        self.address = None
        self.type = None
        self.format = None
        self.size = None


class Spider80s:
    """
    爬虫
    """

    def __init__(self) -> None:
        self.url = 'https://www.80s.tt/'
        self._movies = list()
        self._request = requests.session()
        self._request.verify = False
        self._load()

    def _load(self):
        response = self._request.get(self.url)
        self.url = response.url
        self._request.close()

    def _search_item(self):
        """
        打开搜索页面，搜索电影
        :return:
        """
        for _mov in MOVIES:
            _LOG.info('开始搜索[{}]'.format(_mov))
            data = {'keyword': _mov}
            response = self._request.request('POST', '{}/search'.format(self.url), data=data)
            self._parse_search_list(response.text, _mov)
        self._request.close()

    def _parse_search_list(self, html, name):
        """
        解析搜索页面电影
        :return:
        """
        bs_obj = BeautifulSoup(html, 'lxml')
        serach_list = bs_obj.select('a.list-group-item')
        select = lambda tag, index: str.strip(tag.select('h4')[0].get_text().split('\n')[index])
        for mov in serach_list:
            if name == select(mov, 2):
                _movie = Movie()
                _movie.name = name
                _movie.id = re.search('[0-9]+', mov.get('href')).group()
                _movie.type = select(mov, 1)
                _movie.year = select(mov, 3)
                _movie.rank = select(mov, 4)
                if _movie.id:
                    _movie.downloads = self._parse_page(_movie.id)
                self._movies.append(_movie)

    def _parse_page(self, page_id) -> list:
        """
        解析电影/电视剧页面
        :return:
        """
        md_list = []
        response = self._request.request(
            method='GET',
            url='{}/movie/{}'.format(self.url, page_id)
        )
        if response.status_code == 200:
            self._request.close()
            _LOG.info('发现下载页,开始解析:{}'.format('{}/movie/{}'.format(self.url, page_id)))
            return self.parse_downloads_urls(response.text)
        return md_list

    def parse_downloads_urls(self, html):
        _movies = []
        bs_obj = BeautifulSoup(html, "lxml")
        files = bs_obj.select('#files')[0].select('div.td-dl-links')
        select = lambda tag, key: tag.select('span.{}'.format(key))
        for file in files:
            movie = MovieDownload()
            movie.name = file.a.get_text()
            movie.type = file.findAll('span', {'class': re.compile('label-quality.*')})[0].get_text()
            movie.format = select(file, 'label-ext-1')[0].get_text() if select(file, 'label-ext-1') else None
            movie.size = select(file, 'label-filesize')[0].get_text() if select(file, 'label-filesize') else None
            movie.address = file.a.get('href')
            _movies.append(movie)
        return _movies

    def _output_movies(self):
        """
        输出电影信息到文件
        :return:
        """
        if not self._movies:
            _LOG.info("Sorry,80s未搜索到下载地址.")
        for _mov in self._movies:
            _LOG.info("\n{}[{}][{}][{}]\n".format(_mov.name, _mov.type, _mov.year, _mov.rank))
            file = '{}-{}.txt'.format(_mov.name, _mov.id)
            with open(file, 'w', encoding='utf-8') as writer:
                text = '\n'.join(_mov.get_urls())
                _LOG.info(text)
                writer.writelines(text)
            _LOG.info("\n-->输出文件:{}".format(file))

    def run(self):
        """
        运行爬虫
        :return:
        """
        self._search_item()
        self._output_movies()


def main():
    requests.packages.urllib3.disable_warnings()
    mov_list = sys.argv[1:]
    MOVIES.extend(mov_list)
    spider = Spider80s()
    spider.run()


if __name__ == '__main__':
    main()
