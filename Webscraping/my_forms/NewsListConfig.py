from django import forms


class NewsListConfigv2(forms.Form):
    newsListConfig_host = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Host'}), label='Host')
    newsListConfig_newsListLink = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'newsListLink'}), label='newsListLink')
    newsListConfig_newsList = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'newsList'}), label='newsList')
    newsListConfig_link = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'link'}), label='link')
    newsListConfig_title = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'title'}), label='title')
    newsListConfig_img = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'img '}), label='img ')
    newsListConfig_category = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'category'}), label='category')
