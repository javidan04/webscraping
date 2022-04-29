from core.Scraping import Scraping
from SiteScraping import Config
from SiteScraping import XpathConfig
from SiteScraping import SiteScraping
import config
allSiee = config.siteConfig()
for host,siteConfig in allSiee.items():
    config =Config()
    config.host = host

    x = XpathConfig()
    newsListLink = siteConfig["xpath"]["newsListConfig"]["newsListLink"]
    x.newsList = siteConfig["xpath"]["newsListConfig"]["newsList"]
    x.title = siteConfig["xpath"]["newsListConfig"]["title"]
    x.link = siteConfig["xpath"]["newsListConfig"]["link"]
    x.img = siteConfig["xpath"]["newsListConfig"]["img"]

    site = SiteScraping(newsListLink, x,config)

    newsConfigXpath = XpathConfig()
    newsConfigXpath.title = siteConfig["xpath"]["newsConfig"]["title"]
    newsConfigXpath.category = siteConfig["xpath"]["newsConfig"]["category"]
    newsConfigXpath.img = siteConfig["xpath"]["newsConfig"]["img"]
    newsConfigXpath.content = siteConfig["xpath"]["newsConfig"]["content"]
    newsConfigXpath.content_date_time = siteConfig["xpath"]["newsConfig"]["content_date_time"]
    site.xpathConfigReadNews = newsConfigXpath
    Scraping(site)