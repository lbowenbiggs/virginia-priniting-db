from django.conf.urls import url
from . import views

app_name = 'VPDB'
urlpatterns = [
    # ex: /VPDB/
    url(r'^$', views.index, name='index'),
    # ex: /VPDB/news_cite/1/
    url(r'^news_cite/(?P<obj_id>[0-9]+)/$', views.news_cite_detail, name='news_cite_detail')
]