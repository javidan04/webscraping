from WebScrapingApp.core.Scraping import Scraping
from WebScrapingApp.SiteScraping import Config
from WebScrapingApp.SiteScraping import XpathConfig
from WebScrapingApp.SiteScraping import SiteScraping


class ProdWebScrapping:
    @classmethod
    def run(cls, x, newsXpath):
        config = Config()
        config.host = x.host
        config.newsListStaticImgUrl = x.newsListStaticImgUrl
        config.newsListStaticLinkUrl = x.newsListStaticLinkUrl
        config.newsStaticImgUrl = x.newsStaticImgUrl
        site = SiteScraping(x.newsListLink, x, config)
        site.xpathConfigReadNews = newsXpath
        Scraping(site)
