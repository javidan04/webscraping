def siteConfig():
    return {
        "apa_az":{
            "xpath":{
                "newsListConfig": {
                    "newsListLink":"https://apa.az/az/butun-xeberler",
                    "newsList":"//div[@class='four_columns_block mt-site']//a",
                    "link":"@href",
                    "title":"div//h1[@class='title']/text()",
                    "img":"div[@class='img']//img/@src",
                },
                "newsConfig": {
                    "category": '//main/div[@class="container"]/div/h3/text()',
                    "title": "//div[@class='news_main']/div[@class='content_main']/h1[@class='title_news mb-site']/text() | //div[@class='news_main']/div[@class='content_main']/h3/text()",
                    "content": '//div[@class="news_main"]/div[@class="content_main"]/div[@class="news_content mt-site"]/div[@class="texts mb-site"]/p//text()',
                    "img": '//div[@class="news_main"]/div[@class="content_main"]/div[@class="main_img"]/img/@src',
                    "content_date_time": '//div[@class="news_main"]/div[@class="content_main"]/div[@class="date_news"]//span[@class="date"]/text()',
                }
            }

        },
        "trend.az": {
            "xpath": {
                "newsListConfig": {
                    "newsListLink": "https://az.trend.az/archive/",
                    "newsList": "//div[@class='category-news-wrapper']/div[@class='category-article']",
                    "link": "a[@class='article-link']/@href",
                    "title": "a[@class='article-link']/span[@class='article-title']/text()",
                    "img": "a[@class='article-link']/figure/img/@src",
                },
                "newsConfig": {
                    "category": '//article/div[@class="article-header"]/ul/li[2]/a/text()',
                    "title": "//article/div[@class='article-header']/h1/text()",
                    "content": "//article/div[@class='article-content-wrapper']/div[@class='article-body-wrapper']/div[@class='article-body']/div[@class='article-text']/p/text()",
                    "img": "//article/div[@class='article-content-wrapper']/div[@class='article-body-wrapper']/div[@class='article-body']/img[@class='article-image']/@src",
                    "content_date_time": '//article/div[@class="article-header"]/div[@class="article-meta"]/span[@class="date"]/text()',
                    "content_video": '//article//div[@class="article-body"]//iframe/@src',
                    "content_img": '//article//div[@class="article-gallery"]//img/@src',
                }
            }

        }
    }