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
import datetime
import time

today = date.today()

Session = sessionmaker(bind=engine.connect_mysql())
session = Session()


def newsLists(no):
    URL = "https://aqreqator.az/xeberYukleD.php"
    page = requests.post(URL, data={'sehife': no,"nov":"xeberler"})
    soup = BeautifulSoup(page.content, "html.parser")
    news = []
    try:
        results = soup
        job_elements = results.find_all("div", class_="ts-grid-box")

        for job_element in job_elements:
            item = dict()

            try:
                titleTag  = job_element.find("h3", class_="post-title")
                hrefTag   =  job_element.find("h3", class_="post-title").find("a")
                dateTag   =  job_element.find("span", class_="post-date-info")
                category   =  job_element.find("a", class_="post-cat")
                item["title"] = titleTag.text.strip() if titleTag else None
                item["href"] = hrefTag["href"] if hrefTag else None
                item["date"] = today.strftime("%Y-%m-%d")+" "+dateTag.text.strip() if dateTag else None
                item["category"] = category.text if category else ""
                item["tarix"] = today.strftime("%Y-%m-%d")+" "+dateTag.text.strip() if dateTag else today.strftime("%Y-%m-%d")
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
            except Exception as e:
                print(str(e))
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
    print("start read :" + url)
    news_contenet_count = session.query(Tables.NewsContent).filter(Tables.NewsContent.link == url).count()
    if (news_contenet_count == 0):
        page = requests.get(url)
        item = dict()
        soup = BeautifulSoup(page.content, "html.parser")
        try:
            resultsHead = soup.find("div", class_="entry-header")
            resultsContent = soup.find("div", class_="post-content-area")
            titleTag = resultsHead.find("meta", itemprop="headline")
            contet = resultsContent.find("div", class_="entry-content")
            dateTag = resultsHead.find("meta", itemprop="dateModified")
            host = resultsHead.find("meta", itemprop="name")
            link = resultsHead.find("span", itemprop="publisher")
            if link:
                link = link.find("a")
            imgTag = resultsContent.find("img", itemprop="image")

            if not titleTag: titleTag = results.find("h3", class_="title_news mb-site")
            item["title"] = titleTag["content"] if titleTag else None
            item["img"] = imgTag["src"] if imgTag else None
            item["date"] = dateTag["content"] if dateTag else None
            item["host"] = host["content"] if host else None
            item["link"] = link["href"] if link else None
            item["contet"] = contet.text if contet else None
            item["category"] = ""
            item["tarix"] = today.strftime("%Y-%m-%d")
            item["time"] = int(time.mktime(datetime.datetime.strptime(item["date"],'%Y-%m-%d %H:%M:%S').timetuple()))
            print(item)
            if (news_contenet_count == 0):
                new_news_contenet = Tables.NewsContent(
                    link=item["link"],
                    title=item["title"],
                    categori=item["category"],
                    contetn=item["contet"],
                    tarix=item["tarix"],
                    data=item["date"],
                    host=item["host"],
                    img=item["img"],
                    time=item["time"])
                try:
                    session.add(new_news_contenet)
                    session.commit()
                    news_update = session.query(Tables.News).get(news.id)
                    news_update.status = 1
                    session.commit()
                except Exception as e:
                    print(str(e))
                    print("DB add error")
                finally:
                    print("DB inserted")
            else:
                print(news_contenet_count)
                print(item)
        except Exception as e:
            print(str(e))
            print("Something went wrong")
        finally:
            print("end read :" + url)
            print("*" * 20)
    else:
        print("Oxunub ")
        print(news_contenet_count)
        print("(->>><<<-) " * 20)



def read():
    for i in range(1,50):
        news_items = newsLists(i)
        not_read = session.query(Tables.News) \
            .filter(
            and_(
                Tables.News.link.like('%aqreqator.az%'),
                Tables.News.status == 0
            )
        )
        for news in not_read:
            try:
                read_news_items(news)
            except Exception as e:
                print(str(e))
                print("Something went wrong")
            finally:
                print("read_news_items")
        print("*"*1000)
        print("*"*1000)
        print("*"*1000)
        print("S L E E P")
        print("*" * 1000)
        print("*" * 1000)
        print("*" * 1000)
        time.sleep(10)

read()

