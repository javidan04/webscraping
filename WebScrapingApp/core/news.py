class News:
    __host: str = None
    __link: str = None
    __title: str = None
    __category: str = None
    __subcategory: str = None
    __content: str = None
    __main_image: str = None
    __content_image: str = None
    __content_video: str = None
    __date_time: str = None
    __content_date_time: str = None

    @property
    def host(self) -> str:
        return self.__host

    @host.setter
    def host(self, host: str):
        self.__host = host

    @property
    def link(self) -> str:
        return self.__link

    @link.setter
    def link(self, link: str):
        self.__link = link

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title.strip()

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category):
        self.__category = category

    @property
    def subcategory(self):
        return self.__subcategory

    @subcategory.setter
    def subcategory(self, subcategory):
        self.__subcategory = subcategory

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content.strip()

    @property
    def main_image(self):
        return self.__main_image

    @main_image.setter
    def main_image(self, main_image):
        self.__main_image = main_image

    @property
    def content_image(self):
        return self.__content_image

    @content_image.setter
    def content_image(self, content_image):
        self.__content_image = content_image

    @property
    def content_video(self):
        return self.__content_video

    @content_video.setter
    def content_video(self, content_video):
        self.__content_video = content_video

    @property
    def date_time(self):
        return self.__date_time

    @date_time.setter
    def date_time(self, date_time):
        self.__date_time = date_time

    @property
    def content_date_time(self):
        return self.__content_date_time

    @content_date_time.setter
    def content_date_time(self, content_date_time):
        self.__content_date_time = content_date_time





