from django import forms
from Webscraping.models import News
from Webscraping.models import NewsListConfigModel


class EmpForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"


class NewsListConfig(forms.ModelForm):
    class Meta:
        model = NewsListConfigModel
        fields = "__all__"


class NewsConfig(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"

class NewsListConfigForm(forms.ModelForm):
    newsListConfig_host = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Host'}), label='Host')
    newsListConfig_newsListLink = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'newsListLink'}), label='newsListLink')
    newsListConfig_newsList = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'newsList'}), label='newsList')
    newsListConfig_link = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'link'}), label='link')
    newsListConfig_link_static_text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'link'}), label='static link' , required=False)
    newsListConfig_title = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'title'}), label='title')
    newsListConfig_img = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'img '}), label='img ')
    newsListConfig_img_static_text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'static img link'}), label='img ' , required=False )
    newsListConfig_category = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'category'}), label='category')

    class Meta:
        model = NewsListConfigModel
        fields = "__all__"

class NewsConfigForm(forms.ModelForm):
    newsConfig_host = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Host'}), label='Host')
    newsConfig_category = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'category'}), label='category')
    newsConfig_title = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'title'}), label='title')
    newsConfig_content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Content'}), label='Content')
    newsConfig_img = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'img '}), label='img ')
    newsConfig_img_static_text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'static img link'}),label='img ' , required=False)
    newsConfig_content_date_time = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'date_time'}),label='date_time ')
    newsConfig_content_video = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'content_video'}),label='content_video')
    newsConfig_content_img = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'content_img'}),label='content_img ')

    class Meta:
        model = News
        fields = "__all__"
