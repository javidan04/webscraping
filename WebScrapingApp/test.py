from WebScrapingApp.core.Scraping import Scraping
from WebScrapingApp.TestSiteScraping import Config
from WebScrapingApp.TestSiteScraping import XpathConfig
from WebScrapingApp.TestSiteScraping import SiteScraping
import WebScrapingApp.testConfig


class Test:
    @classmethod
    def runn(cls):
        allSiee = WebScrapingApp.testConfig.siteConfig()
        for host, siteConfig in allSiee.items():
            config = Config()
            config.host = host

            x = XpathConfig()
            newsListLink = siteConfig["xpath"]["newsListConfig"]["newsListLink"]
            x.newsList = siteConfig["xpath"]["newsListConfig"]["newsList"]
            x.title = siteConfig["xpath"]["newsListConfig"]["title"]
            x.link = siteConfig["xpath"]["newsListConfig"]["link"]
            x.img = siteConfig["xpath"]["newsListConfig"]["img"]
            site = SiteScraping(newsListLink, x, config)
            site.newsLists()

            newsConfigXpath = XpathConfig()
            newsConfigXpath.title = siteConfig["xpath"]["newsConfig"]["title"]
            newsConfigXpath.category = siteConfig["xpath"]["newsConfig"]["category"]
            newsConfigXpath.img = siteConfig["xpath"]["newsConfig"]["img"]
            newsConfigXpath.content = siteConfig["xpath"]["newsConfig"]["content"]
            newsConfigXpath.content_date_time = siteConfig["xpath"]["newsConfig"]["content_date_time"]
            # newsConfigXpath.content_video = siteConfig["xpath"]["newsConfig"]["content_video"]
            # newsConfigXpath.content_img = siteConfig["xpath"]["newsConfig"]["content_img"]

            site.xpathConfigReadNews = newsConfigXpath
            newsLists = []
            for i in site.news_list:
                #print("*" * 100)
                attrs = vars(i)
                #print(':\n'.join("%s: %s" % item for item in attrs.items()))
                #print("*" * 100)
                #print("===" * 100)
                readNews = site.readNews(i)
                attrs = vars(readNews)
                #print(':\n'.join("%s: %s" % item for item in attrs.items()))
                #print("===" * 100)
                newsLists.append(readNews)
                break
            return newsLists

    @classmethod
    def newsListConfig(cls,x):
        config = Config()
        config.host = x.host
        config.newsListStaticImgUrl = x.newsListStaticImgUrl
        config.newsListStaticLinkUrl = x.newsListStaticLinkUrl
        config.newsStaticImgUrl = x.newsStaticImgUrl
        site = SiteScraping(x.newsListLink, x, config)
        site.newsLists()
        return site.news_list

    @classmethod
    def newsConfig(cls,x,newsConfigXpath,limit):
        config = Config()
        config.host = x.host
        config.newsListStaticImgUrl = x.newsListStaticImgUrl
        config.newsListStaticLinkUrl = x.newsListStaticLinkUrl
        config.newsStaticImgUrl = x.newsStaticImgUrl
        site = SiteScraping(x.newsListLink, x, config)
        site.newsLists()
        site.xpathConfigReadNews = newsConfigXpath
        newsLists = []
        count = 0
        for i in site.news_list:
            readNews = site.readNews(i)
            newsLists.append(readNews)
            if count > limit:
                break
            count += 1
        return newsLists

