from __future__ import unicode_literals
from django.db import models


class NewsListConfigModel(models.Model):
    newsListConfig_host = models.CharField(max_length=2500)
    newsListConfig_newsListLink = models.CharField(max_length=2500)
    newsListConfig_newsList = models.CharField(max_length=2500)
    newsListConfig_link = models.CharField(max_length=2500)
    newsListConfig_link_static_text = models.CharField(max_length=2500)
    newsListConfig_title = models.CharField(max_length=2500)
    newsListConfig_img = models.CharField(max_length=2500)
    newsListConfig_img_static_text = models.CharField(max_length=2500)
    newsListConfig_category = models.CharField(max_length=2500)
    status = models.IntegerField()
    allow = models.IntegerField()
    readCount = models.IntegerField()

    class Meta:
        db_table = "newsListConfig"


class News(models.Model):
    newsConfig_host = models.CharField(max_length=2500)
    newsConfig_category = models.CharField(max_length=2500)
    newsConfig_title = models.CharField(max_length=2500)
    newsConfig_content = models.CharField(max_length=2500)
    newsConfig_img = models.CharField(max_length=2500)
    newsConfig_content_date_time = models.CharField(max_length=2500)
    newsConfig_content_video = models.CharField(max_length=2500)
    newsConfig_content_img = models.CharField(max_length=2500)
    newsConfig_img_static_text = models.CharField(max_length=2500)
    status = models.IntegerField()

    class Meta:
        db_table = "newsConfig"


class WebScrapingDataModel(models.Model):
    id = models.IntegerField(primary_key=id)
    host = models.TextField()
    link = models.TextField()
    title = models.TextField()
    category = models.TextField()
    subcategory = models.TextField()
    content = models.TextField()
    main_image = models.TextField()
    content_image = models.TextField()
    content_video = models.TextField()
    date_time = models.DateTimeField()
    content_date_time = models.TextField()
    type = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = "web_scraping_data"
