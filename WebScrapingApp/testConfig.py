"""nyusinfo.az":{
            "xpath":{
                "newsListConfig": {
                    "newsListLink":"https://azinfo.tv/",
                    "newsList":"//div[@class='sagIcerik1']",
                    "link":"a/@href",
                    "title":"//div[@class='sagIcerikyazi']/strong/text()",
                    "img":"//img/@src",
                },
                "newsConfig": {
                    "category": '//div[@class="sol2"]//font/text()',
                    "title": "//div[@class='sol2']//div[@class='haberBaslik']/h1/text()",
                    "content": "//div[@class='sol2']//div[@class='haberText']//text()",
                    "img": "//div[@class='sol2']//div[@class='haberText']//img/@src",
                    "content_date_time": '//div[@class="sol2"]//font/text()',
                    "content_video": '//div[@class="sol2"]//font/text()',
                    "content_img": '//div[@class="sol2"]//font/text()',
                }
            }

        },"""
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
    }