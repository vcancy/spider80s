__author__ = "vcancy"
"""
80s电影爬虫，爬取给定电影/电视剧的迅雷下载地址，输出到对应文件
"""

# /usr/bin/python
# -*-coding:utf-8-*-
movies = ['远大前程']


class Spider80s:
    """
    爬虫
    """

    def __init__(self) -> None:
        self.url = 'https://www.80s.tt/'
        self.search_url = f'{self.search_url}/search'
        self.page_url = f'{self.search_url}/movie'
        self._movies = list()

    def _search_item(self):
        """
        打开搜索页面，搜索电影
        :return:
        """
        pass

    def _parse_search_list(self):
        """
        解析搜索页面电影
        :return:
        """
        pass

    def _parse_page(self) -> dict:
        """
        解析电影/电视剧页面
        :return:
        """
        pass

    def _output_movies(self):
        """
        输出电影信息到文件
        :return:
        """
        pass

    def run(self):
        """
        运行爬虫
        :return:
        """
        pass


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


class MovieDownload:
    """
    电影/电视剧下载信息
    """

    def __init__(self) -> None:
        self.id = None
        self.name = None
        self.address = None
        self.type = None
        self.format = None
        self.size = None
