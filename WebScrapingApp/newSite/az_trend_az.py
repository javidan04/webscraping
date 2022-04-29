# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
from bs4 import BeautifulSoup
import db.WebScraping as Tables
import db.engine as engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from datetime import date
import time

today = date.today()

Session = sessionmaker(bind = engine.connect_mysql())
session = Session()


def newsLists():
    URL = "https://az.trend.az/archive/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    news = []
    try:
        results = soup.find("div", class_="category-news-wrapper")
        job_elements = results.find_all("div", class_="category-article")

        for job_element in job_elements:
            item = dict()
            try:
                titleTag = job_element.find("span", class_="article-title")
                hrefTag = job_element.find("a",class_="article-link")
                dateTag = job_element.find("span", class_="article-date")
                categoryTag = job_element.find("span", class_="article-category")

                item["title"] = titleTag.text if titleTag else None
                item["href"] = hrefTag["href"] if hrefTag else None
                item["date"] = dateTag.text if dateTag else None
                item["category"] = categoryTag.text if categoryTag else None
                item["tarix"] = today.strftime("%Y-%m-%d")
                item["time"] = int(time.time())
                news.append(item)
                news_count = session.query(Tables.News).filter(Tables.News.link == item["href"]).count()
                if (news_count == 0):
                    new_news = Tables.News(
                        link=item["href"],
                        title=item["title"],
                        categori=item["category"],
                        tarix=item["tarix"],
                        data=item["date"],
                        status=0,
                        time=item["time"])
                    try:
                        session.add(new_news)
                        session.commit()
                    except:
                        print("DB add error")
                    finally:
                        print("DB inserted")
                else:
                    print(news_count)
                print(item)
                print("**********")
            except:
                print("Something went wrong")
            finally:
                print("--" * 20)
    except Exception as e:
        print(str(e))
        print("Something went wrong")
    finally:
        print("end read :" + URL)
        print("*" * 20)
    return news


def read_news_items(news):
    url = news.link
    print("start read :"+url)
    page = requests.get(url)
    item = dict()
    soup = BeautifulSoup(page.content, "html.parser")
    try:
        results = soup.find("article", class_="article alt")
        titleTag = results.find("h1",class_="article-title")
        category = results.find("a", class_="category-link")
        contet = results.find("div", class_="article-text")
        dateTag = results.find("span", class_="date")
        imgTag = results.find("img", class_="article-image")

        if not titleTag : titleTag = results.find("h3", class_="title_news mb-site")
        item["title"] = titleTag.text if titleTag else None
        item["img"] = imgTag["src"] if imgTag else None
        item["date"] = dateTag.text if dateTag else None
        item["contet"] = contet.text if contet else None
        item["category"] = category.text if category else None
        item["tarix"] = today.strftime("%Y-%m-%d")
        item["time"] = int(time.time())
        news_contenet_count = session.query(Tables.NewsContent).filter(Tables.NewsContent.link == url).count()
        if (news_contenet_count == 0):
            new_news_contenet = Tables.NewsContent(
                link=url,
                title=item["title"],
                categori=item["category"],
                contetn=item["contet"],
                tarix=item["tarix"],
                data=item["date"],
                host="az.trend.az",
                time=item["time"])
            try:
                session.add(new_news_contenet)
                session.commit()
                news_update = session.query(Tables.News).get(news.id)
                news_update.status = 1
                session.commit()
            except Exception as e:
                print(str(e))
                print("Something went wrong")
            finally:
                print("DB inserted")

        else:
            print(news_contenet_count)
        print(item)
    except Exception as e:
        print(str(e))
        print("Something went wrong")
    finally:
        print("end read :"+url)
        print("*"*20)


def read():
    news_items = newsLists()
    not_read = session.query(Tables.News) \
        .filter(
        and_(
            Tables.News.link.like('%az.trend.az%'),
            Tables.News.status == 0
        )
    )
    for news in not_read:
        read_news_items(news)

