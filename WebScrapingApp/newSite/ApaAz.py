from core.site import Site
from core.news import News
from datetime import date


class ApaAz(Site):

    def __init__(self, news_lists_url):
        super().__init__(news_lists_url)

    def newsLists(self):
        content = self.main_page_content.find("div", class_="four_columns_block mt-site")
        job_elements = content.find_all("a", class_="item")
        for job_element in job_elements:
            try:
                create_news = News()
                create_news.host = "apa_az.config"
                create_news.title = job_element.find("div", class_="content").text
                create_news.link = job_element["href"]
                create_news.content_date_time = job_element.find("div", class_="content").text
                create_news.date_time = date.today().strftime("%Y-%m-%d")
                self.news_list.append(create_news)
            except Exception as e:
                print(str(e))

    def readNews(self, news: News):
        print("start read :" + news.link)
        content = self.getPageContent(news.link)
        try:
            today = date.today()
            news_article = content.find("div", class_="news_main")
            titleTag = news_article.find("h1", class_="title_news mb-site")
            content = news_article.find("div", class_="news_content mt-site")
            dateTag = news_article.find("div", class_="date_news")
            imgTag = news_article.find("img")

            if not titleTag: titleTag = news_article.find("h3", class_="title_news mb-site")
            news.title = titleTag.text if titleTag else None
            news.main_image = imgTag["src"] if imgTag else None
            news.content_date_time = dateTag.text if dateTag else None
            news.content = content.text if content else None
            news.date_time = today.strftime("%Y-%m-%d")
        except Exception as e:
            print(str(e))
            print("Something went wrong")
        finally:
            print("end read :" + news.link)
            print("*" * 20)
        return news




