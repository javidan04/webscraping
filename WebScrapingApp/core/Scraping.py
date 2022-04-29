from WebScrapingApp.core.site import Site
from WebScrapingApp.model import NewsModel


class Scraping:
    def __init__(self,site: Site):
        self.site = site
        self.mainPageScraping()

    def mainPageScraping(self):
        self.site.newsLists()
        for news in self.site.news_list:
            try:
                new_news_model = NewsModel.NewsModel()
                new_news_model.save(news)
                new_news_model.saveDate(self.site.readNews(news))
            except Exception as e:
                print(str(e))

