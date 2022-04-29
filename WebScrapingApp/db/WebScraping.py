from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class WebScrapingData(Base):
    __tablename__ = 'web_scraping_data'
    id = Column(Integer, primary_key=True)
    host = Column(String)
    link = Column(String)
    title = Column(String)
    category = Column(String)
    subcategory = Column(String)
    content = Column(String)
    main_image = Column(String)
    content_image = Column(String)
    content_video = Column(String)
    date_time = Column(DateTime)
    content_date_time = Column(String)
    type = Column(Integer)
    status = Column(Integer)


class WebScrapingLink(Base):
    __tablename__ = 'web_scraping_link'
    id = Column(Integer, primary_key=True)
    host = Column(String)
    link = Column(String)
    title = Column(String)
    category = Column(String)
    subcategory = Column(String)
    main_image = Column(String)
    date_time = Column(DateTime)
    content_date_time = Column(String)
    type = Column(Integer)
    status = Column(Integer)
