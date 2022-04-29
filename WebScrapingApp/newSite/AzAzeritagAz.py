from core.site import Site
from core.news import News
from datetime import date


class AzAzeritagAz(Site):

    def __init__(self, news_lists_url):
        super().__init__(news_lists_url)

    def newsLists(self):
        content = self.main_page_content.find("div", class_="content-inner clear")
        job_elements = content.find_all("div", class_="news-item")
        for job_element in job_elements:
            try:
                create_news = News()
                create_news.host = "apa_az.config"
                create_news.title = job_element.find("h1", class_="news-title").text
                create_news.link = "https://azertag.az"+job_element.find("a")["href"]
                create_news.content_date_time = job_element.find("div", class_="news-date").text
                create_news.date_time = date.today().strftime("%Y-%m-%d")
                self.news_list.append(create_news)
            except Exception as e:
                print(str(e))

    def readNews(self, news: News):
        print("start read :" + news.link)
        content = self.getPageContent(news.link)
        try:
            today = date.today()
            results = content.find("div", id="content-article")
            titleTag = results.find("h1", class_="content-title")
            contet = results.find("div", id="selectedtext")
            dateTag = results.find("div", class_="news-date")
            imgTag = results.find("img")

            news.title = titleTag.text
            news.main_image = "https://azertag.az/" + imgTag["src"] if imgTag else None
            news.content_date_time = dateTag.text if dateTag else None
            news.content = contet.text if content else None
            news.date_time = today.strftime("%Y-%m-%d")
        except Exception as e:
            print(str(e))
            print("Something went wrong")
        finally:
            print("end read :" + news.link)
            print("*" * 20)
        return news




