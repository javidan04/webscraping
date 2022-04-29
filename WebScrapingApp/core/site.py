from WebScrapingApp.core.news import News
import requests
from requests import Session
from collections import OrderedDict
from bs4 import BeautifulSoup
import lxml.html


class Site:
    news_lists_url: str
    news_list: list = []
    main_page_content: BeautifulSoup

    def __init__(self, news_lists_url):
        self.news_lists_url = news_lists_url
        self.readMainPage()
        self.session = Session()
        headers = OrderedDict({
            'Accept-Encoding': 'gzip, deflate',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        })
        self.session.headers = headers

    def readMainPage(self):
        self.main_page_content = self.getPageContent(self.news_lists_url)

    def requests(self, url):
        try:
            r = requests.get(url,headers=self.session.headers)
            print(url+": status_code:",r.status_code)
            print(url+": status_code:",r.headers)
            return r.content
        except Exception as e:
            print(e)
            return "<div>ERROR</div>"

    def getPageContent(self, url):
        page = self.requests(url)
        BeautifulSoup(page, "html.parser")

    def getLXnl(self, url):
        page = self.requests(url)
        self.main_page_content = lxml.html.fromstring(page)
        return self.main_page_content

    def removeElement(self, xpath):
        for bad in xpath:
            bad.getparent().remove(bad)
        return xpath

    def newsLists(self):
        pass

    def readNews(self, news: News):
        pass

    def saveNewsList(self, news: News):
        pass
