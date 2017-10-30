from django.conf.urls import url
from . import views

app_name = 'VPDB'
urlpatterns = [
    # ex: /VPDB/
    url(r'^$', views.index, name='index'),
    # ex: /VPDB/news_cite/1/
    url(r'^news_cite/(?P<pk>[0-9]+)/$', views.NewsCiteDetailView.as_view(), name='news_cite_detail'),
    # ex: /VPDB/news_hist/1/
    url(r'^news_hist/(?P<pk>[0-9]+)/$', views.NewsHistDetailView.as_view(), name='news_hist_detail'),
    # ex: /VPDB/bio/1/
    url(r'^bio/(?P<pk>[0-9]+)/$', views.BioDetailView.as_view(), name='bio_detail'),
]
