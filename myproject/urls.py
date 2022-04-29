from django.contrib import admin
from django.urls import path

from Webscraping import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('runCronJob/<int:id>', views.runCronJob),
    path('WebScrapingData/<str:host>', views.WebScrapingData),
    path('WebScrapingData/show/<int:id>', views.WebScrapingDataShow),
    path('newsListConfig/', views.newsListConfig),
    path('/', views.index),
    path('site/list', views.siteList),
    path('site/list/<int:id>', views.newsListConfigEdit),
]
