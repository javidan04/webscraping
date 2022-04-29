import WebScrapingApp.db.WebScraping as WebScraping
import WebScrapingApp.core.news
import WebScrapingApp.db.engine as engine
from sqlalchemy.orm import sessionmaker


class NewsModel:
    def __init__(self):
        Session = sessionmaker(bind=engine.connect_mysql())
        self.session = Session()

    def save(self, news: WebScrapingApp.core.news.News):
        news_count = self.session.query(WebScraping.WebScrapingLink).filter(
            WebScraping.WebScrapingLink.link == news.link
        ).count()
        if news_count == 0:
            new_news = WebScraping.WebScrapingLink(
                host=news.host,
                link=news.link,
                title=news.title,
                category=news.category,
                subcategory=news.subcategory,
                main_image=news.main_image,
                date_time=news.date_time,
                content_date_time=news.content_date_time,
                type=1,
                status=1,
            )
            try:
                self.session.add(new_news)
                self.session.commit()
            except Exception as e:
                print(str(e))
            finally:
                print("DB ++++")
        else:
            print(news_count)

    def saveDate(self, news: WebScrapingApp.core.news.News):
        news_content_count = self.session.query(WebScraping.WebScrapingData).filter(
            WebScraping.WebScrapingData.link == news.link
        ).count()
        if news_content_count == 0:
            new_news_content = WebScraping.WebScrapingData(
                host=news.host,
                link=news.link,
                title=news.title,
                category=news.category,
                subcategory=news.subcategory,
                content=news.content,
                main_image=news.main_image,
                content_image=news.content_image,
                content_video=news.content_video,
                date_time=news.date_time,
                content_date_time=news.content_date_time
            )
            try:
                self.session.add(new_news_content)
                self.session.commit()
                news_update = self.session.query(WebScraping.WebScrapingLink).filter(
                    WebScraping.WebScrapingLink.link == news.link
                )
                news_update.status = 1
                self.session.commit()
            except Exception as e:
                print(str(e))
                print("DB add error")
            finally:
                print("DB inserted")
        else:
            print(news_content_count)
            print(news)
