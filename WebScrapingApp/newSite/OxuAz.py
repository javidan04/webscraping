from core.site import Site
from core.news import News


class XpathConfig:
    newsList = ""
    title = ""
    content = ""
    link = ""
    img = ""

class Config:
    pass



class OxuAz(Site):

    def __init__(self, news_lists_url,xpathConfig):
        super().__init__(news_lists_url)
        super().getLXnl(news_lists_url)
        self.xpathConfig = xpathConfig

    def newsLists(self):
        #news_list_node = self.main_page_content.xpath("//section[@class='news-list']/div[@class='news-i']")
        news_list_node = self.main_page_content.xpath(self.xpathConfig.newsList)
        print(news_list_node)
        for job_element in news_list_node:
            try:
                create_news = News()
                create_news.host = "oxu.az"
                # create_news.title = job_element.xpath('a[@class="news-i-inner"]//div[@class="title"]/text()')[0]
                create_news.title = job_element.xpath(self.xpathConfig.title)[0]
                print(job_element.xpath(self.xpathConfig.title))
                #create_news.link = "https://oxu.az/" + job_element.xpath('a[@class="news-i-inner"]/@href')[0]
                create_news.link = job_element.xpath(self.xpathConfig.link)[0]
                print(job_element.xpath(self.xpathConfig.link))

                create_news.main_image = job_element.xpath(self.xpathConfig.img)

                print(job_element.xpath(self.xpathConfig.img))
                #create_news.content_date_time = ""
                #create_news.date_time = date.today().strftime("%Y-%m-%d")
                self.news_list.append(create_news)
            except Exception as e:
                print(str(e))

    def readNews(self, news: News):
        print("start read :" + news.link)
        content = self.getLXnl(news.link)
        try:
            news.title = content.xpath("//div[@class='news-inner']/h1/text() | //div[@class='news-inner']/h3/text()")[0]
            news_content = \
            self.removeElement(content.xpath("//div[@class='news-inner']/h1 | //div[@class='news-inner']/h3"))[0]
            news_content = news_content.xpath("//div[@class='news-inner']/text()")[0]
            print(news_content)
            # news.main_image = imgTag["src"] if imgTag else None
            # news.content_date_time = dateTag.text if dateTag else None
            # news.content = content.text if content else None
            # news.date_time = today.strftime("%Y-%m-%d")*/
        except Exception as e:
            print(str(e))
            print("Something went wrong")
        finally:
            print("end read :" + news.link)
            print("*" * 20)
        return news



