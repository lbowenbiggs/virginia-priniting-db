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
    # ex: /VPDB/imprint/1/
    url(r'^imprint/(?P<pk>[0-9]+.[0-9]+)/$', views.ImprintDetailView.as_view(), name='imprint_detail'),

    # ex: /VPDB/news_cites/
    url(r'^news_cites/$', views.NewsCitesListView.as_view(), name='news_cites_index'),
    # ex: /VPDB/news_hists/
    url(r'^news_hists/$', views.NewsHistsListView.as_view(), name='news_hists_index'),
    # ex: /VPDB/bios/
    url(r'^bios/$', views.BiosListView.as_view(), name='bios_index'),
    # ex: /VPDB/imprints/
    url(r'^imprints/$', views.ImprintsListView.as_view(), name='imprints_index'),
]
