from django.template import loader
# Create your view here.
from django import db
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from Webscraping.form import EmpForm
from Webscraping.form import NewsListConfig
from Webscraping.form import NewsConfig
from Webscraping.models import News
from Webscraping.models import WebScrapingDataModel
from Webscraping.form import NewsListConfigForm
from Webscraping.form import NewsConfigForm
from Webscraping.models import NewsListConfigModel
from WebScrapingApp.TestSiteScraping import XpathConfig

from django.db.models import Count
import datetime


from WebScrapingApp.test import Test
from WebScrapingApp.prod import ProdWebScrapping




def siteList(request):
    context = {}

    # add the dictionary during initialization
    context["dataset"] = NewsListConfigModel.objects.filter(status=1)

    return render(request, 'site/list.html', context)



def WebScrapingData(request,host):
    context = {}

    # add the dictionary during initialization
    context["dataset"] = WebScrapingDataModel.objects.all()
    context["chart"] = WebScrapingDataModel.objects.values('host').annotate(total=Count('host')).order_by()
    context["chart2"] = WebScrapingDataModel.objects.values('id')


    return render(request, 'site/WebScrapingDataList.html', context)

def WebScrapingDataShow(request,id):
    context = {}

    # add the dictionary during initialization
    context["dataset"] = WebScrapingDataModel.objects.filter(id=id)


    return render(request, 'site/WebScrapingDatashow.html', context)


def runCronJob(request,id):
    newsListConfig = NewsListConfigModel.objects.filter(allow=1).order_by('readCount')
    #newsListConfig = NewsListConfigModel.objects.filter(id=id).order_by('readCount')
    for item in newsListConfig:
        item.readCount = item.readCount + 1
        item.save()
        x = XpathConfig()
        x.newsListLink = item.newsListConfig_newsListLink
        x.newsList = item.newsListConfig_newsList
        x.title = item.newsListConfig_title
        x.link = item.newsListConfig_link
        x.img = item.newsListConfig_img
        x.host = item.newsListConfig_host
        x.category = item.newsListConfig_category
        x.newsListStaticImgUrl = item.newsListConfig_img_static_text
        x.newsListStaticLinkUrl = item.newsListConfig_link_static_text



        newsConfiges= News.objects.filter(id=item.id)
        for newsConfig in  newsConfiges:
            newsConfigXpath = XpathConfig()
            newsConfigXpath.title = newsConfig.newsConfig_title
            newsConfigXpath.category = newsConfig.newsConfig_category
            newsConfigXpath.img = newsConfig.newsConfig_img
            newsConfigXpath.content = newsConfig.newsConfig_content
            newsConfigXpath.content_date_time = newsConfig.newsConfig_content_date_time
            newsConfigXpath.content_video = newsConfig.newsConfig_content_video
            newsConfigXpath.content_img = newsConfig.newsConfig_content_img
            newsConfigXpath.newsStaticImgUrl = newsConfig.newsConfig_img_static_text
            ProdWebScrapping.run(x,newsConfigXpath)

        db.connections.close_all()
        break
    return HttpResponse("t")






def index(request):
    newsList = []
    if request.method == "POST":
        form = EmpForm(request.POST)
        x = XpathConfig()
        x.newsListLink = request.POST["newsListConfig_newsListLink"]
        x.newsList = request.POST["newsListConfig_newsList"]
        x.title = request.POST["newsListConfig_title"]
        x.link = request.POST["newsListConfig_link"]
        x.img = request.POST["newsListConfig_img"]


        attrs = vars(x)
        print(':\n'.join("%s: %s" % item for item in attrs.items()))

        newsConfigXpath = XpathConfig()
        newsConfigXpath.title = request.POST["newsConfig_title"]
        newsConfigXpath.category = request.POST["newsConfig_category"]
        newsConfigXpath.img = request.POST["newsConfig_img"]
        newsConfigXpath.content = request.POST["newsConfig_content"]
        newsConfigXpath.content_date_time = request.POST["newsConfig_content_date_time"]
        newsConfigXpath.content_video = request.POST["newsConfig_content_video"]
        newsConfigXpath.content_img = request.POST["newsConfig_content_img"]

        if form.is_valid():
            try:
                newsList= Test.run()

            except:
                newsList = []
        return render(request, 'index2.html', {'form': form,'newsList': newsList})
    else:
        form = EmpForm()
        return render(request, 'index2.html', {'form': form,'newsList': newsList})


def newsConfig(request):
    newsList = []
    if request.method == "POST":
        form = NewsListConfig(request.POST)


        if form.is_valid():
            try:
                x = XpathConfig()
                x.newsListLink = request.POST["newsListConfig_newsListLink"]
                x.newsList = request.POST["newsListConfig_newsList"]
                x.title = request.POST["newsListConfig_title"]
                x.link = request.POST["newsListConfig_link"]
                x.img = request.POST["newsListConfig_img"]
                x.host = request.POST["newsListConfig_host"]
                newsList = Test.newsListConfig(x)
                attrs = vars(x)
                print(':\n'.join("%s: %s" % item for item in attrs.items()))

            except Exception as e:
                print(e)
                newsList = []
        return render(request, 'index2.html', {'form': form, 'newsList': newsList})
    else:
        form = EmpForm()
        return render(request, 'index2.html', {'form': form, 'newsList': newsList})


def newsListConfig(request):
    newsList = []
    formNewsList = NewsListConfigForm()
    formNews = NewsConfigForm()
    if request.method == "POST":
        print(request.POST)
        formNewsList = NewsListConfigForm(request.POST)
        formNews = NewsConfigForm(request.POST)
        x = XpathConfig()
        x.newsListLink = request.POST["newsListConfig_newsListLink"]
        x.newsList = request.POST["newsListConfig_newsList"]
        x.title = request.POST["newsListConfig_title"]
        x.link = request.POST["newsListConfig_link"]
        x.img = request.POST["newsListConfig_img"]
        x.host = request.POST["newsListConfig_host"]
        x.category = request.POST["newsListConfig_category"]
        x.newsListStaticImgUrl = request.POST["newsListConfig_img_static_text"]
        x.newsListStaticLinkUrl = request.POST["newsListConfig_link_static_text"]

        newsConfigXpath = XpathConfig()
        newsConfigXpath.title = request.POST["newsConfig_title"]
        newsConfigXpath.category = request.POST["newsConfig_category"]
        newsConfigXpath.img = request.POST["newsConfig_img"]
        newsConfigXpath.content = request.POST["newsConfig_content"]
        newsConfigXpath.content_date_time = request.POST["newsConfig_content_date_time"]
        newsConfigXpath.content_video = request.POST["newsConfig_content_video"]
        newsConfigXpath.content_img = request.POST["newsConfig_content_img"]
        newsConfigXpath.newsStaticImgUrl = request.POST["newsConfig_img_static_text"]
        newsList = []
        print(request.POST["submit"])
        if request.POST["submit"] == "newsList":
            newsList = Test.newsListConfig(x)
        elif request.POST["submit"] == "news":
            newsList = Test.newsConfig(x,newsConfigXpath,3)
        elif request.POST["submit"] == "newsAll":
            newsList = Test.newsConfig(x, newsConfigXpath, 10000)
        elif request.POST["submit"] == "save":
            print(formNewsList.errors)
            if formNewsList.is_valid():

                instanceNewsList = formNewsList.save()
            if formNews.is_valid():
                   newFormNews = formNews.save(commit=False)
                   newFormNews.id = instanceNewsList.id
                   newFormNews.save()
                   return redirect('/site/list/' + str(instanceNewsList.id))


        else:
            pass

        attrs = vars(x)
        print(':\n'.join("%s: %s" % item for item in attrs.items()))
        print(newsList)

    return render(request, 'index22.html', {'formNewsList': formNewsList,'formNews': formNews, 'newsList': newsList, 'newsListConfigModel': {} , "newsConfigModel": {}})

def newsListConfigEdit(request,id):
    newsList = []
    newsListConfigModel = NewsListConfigModel.objects.get(id=id)
    formNewsList = NewsListConfigForm(request.POST or None, instance=newsListConfigModel)

    newsConfigModel = News.objects.get(id=id)
    formNews = NewsConfigForm(request.POST or None, instance=newsConfigModel)
    if request.method == "POST":


        x = XpathConfig()
        x.newsListLink = request.POST["newsListConfig_newsListLink"]
        x.newsList = request.POST["newsListConfig_newsList"]
        x.title = request.POST["newsListConfig_title"]
        x.link = request.POST["newsListConfig_link"]
        x.img = request.POST["newsListConfig_img"]
        x.host = request.POST["newsListConfig_host"]
        x.category = request.POST["newsListConfig_category"]
        x.newsListStaticImgUrl = request.POST["newsListConfig_img_static_text"]
        x.newsListStaticLinkUrl = request.POST["newsListConfig_link_static_text"]

        newsConfigXpath = XpathConfig()
        newsConfigXpath.title = request.POST["newsConfig_title"]
        newsConfigXpath.category = request.POST["newsConfig_category"]
        newsConfigXpath.img = request.POST["newsConfig_img"]
        newsConfigXpath.content = request.POST["newsConfig_content"]
        newsConfigXpath.content_date_time = request.POST["newsConfig_content_date_time"]
        newsConfigXpath.content_video = request.POST["newsConfig_content_video"]
        newsConfigXpath.content_img = request.POST["newsConfig_content_img"]
        newsConfigXpath.content_img = request.POST["newsConfig_content_img"]
        newsConfigXpath.newsStaticImgUrl = request.POST["newsConfig_img_static_text"]
        newsList = []
        if request.POST["submit"] == "newsList":
            newsList = Test.newsListConfig(x)
        elif request.POST["submit"] == "news":
            newsList = Test.newsConfig(x,newsConfigXpath,3)
        elif request.POST["submit"] == "newsAll":
            newsList = Test.newsConfig(x, newsConfigXpath, 10000)
        elif request.POST["submit"] == "save":
            if formNewsList.is_valid():
                formNewsList.save()
            if formNews.is_valid():
                formNews.save()
        elif request.POST["submit"] == "delete":
            NewsListConfigModel.objects.filter(id=id).update(status=0)
            News.objects.filter(id=id).update(status=0)
            return redirect('/site/list')
        elif request.POST["submit"] == "allow":
            NewsListConfigModel.objects.filter(id=id).update(allow=1)
            return redirect('/site/list/' + str(id))
        elif request.POST["submit"] == "deny":
            NewsListConfigModel.objects.filter(id=id).update(allow=0)
            return redirect('/site/list/'+str(id))
        else:
            pass

        attrs = vars(x)
        print(':\n'.join("%s: %s" % item for item in attrs.items()))
    return render(request, 'index22.html', {'formNewsList': formNewsList,'formNews': formNews, 'newsList': newsList, 'newsListConfigModel': newsListConfigModel , "newsConfigModel": newsConfigModel})


