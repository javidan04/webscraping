from WebScrapingApp.core.site import Site
import WebScrapingApp.core.news


class XpathConfig:
    host = ""
    newsList = ""
    title = ""
    content = ""
    category = ""
    link = ""
    img = ""


class Config:
    host = ""
    newsListStaticLinkUrl = ""
    newsListStaticImgUrl = ""
    newsStaticImgUrl = ""


def getData(element,mod="prod",w = ""):
    textData = ""
    for i in element:
        if mod == "dev":
            print(i)
        else:
            textData += i+w
    return textData





class SiteScraping(Site):

    def __init__(self, news_lists_url, xpathConfig, config):
        super().__init__(news_lists_url)
        super().getLXnl(news_lists_url)
        self.xpathConfig = xpathConfig
        self.xpathConfigReadNews = xpathConfig
        self.config = config

    def newsLists(self):
        news_list_node = self.main_page_content.xpath(self.xpathConfig.newsList)
        print(news_list_node)
        self.news_list = []
        for job_element in news_list_node:
            try:
                create_news = WebScrapingApp.core.news.News()
                create_news.host = self.config.host
                create_news.title = getData(job_element.xpath(self.xpathConfig.title))
                create_news.link = self.config.newsListStaticLinkUrl+getData(job_element.xpath(self.xpathConfig.link))
                create_news.main_image = self.config.newsListStaticImgUrl+getData(job_element.xpath(self.xpathConfig.img))
                create_news.category = getData(job_element.xpath(self.xpathConfig.category))
                self.news_list.append(create_news)
            except Exception as e:
                print(str(e))

    def readNews(self, news: WebScrapingApp.core.news.News):
        print("start read :" + news.link)
        content = self.getLXnl(news.link)
        try:
            news.title = getData(content.xpath(self.xpathConfigReadNews.title))
            news.content = getData(content.xpath(self.xpathConfigReadNews.content))
            news.main_image = self.config.newsStaticImgUrl+getData(content.xpath(self.xpathConfigReadNews.img))
            news.category = getData(content.xpath(self.xpathConfigReadNews.category))
            news.content_date_time = getData(content.xpath(self.xpathConfigReadNews.content_date_time))
            news.content_video = getData(content.xpath(self.xpathConfigReadNews.content_video),w=",")
            news.content_image = getData(content.xpath(self.xpathConfigReadNews.content_img),w=",")

        except Exception as e:
            print(str(e))
            print("Something went wrong")
        finally:
            print("end read :" + news.link)
            print("*" * 20)
        return news

