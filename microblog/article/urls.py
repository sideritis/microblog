from django.conf.urls import url
from django.views.decorators.cache import cache_page
from django.conf import settings

from .views import ArticleListView, ArticleDetailView, ArticleAuthorListView, LatestArticlesFeed, \
    ArticlePreviewView, SearchView

urlpatterns = [
    url(r'preview/(?P<pk>\d+)/$', ArticlePreviewView.as_view(), name='preview'),
    url(r'^$', cache_page(settings.CACHE_TIME)(ArticleListView.as_view()), name='list'),
    url(r'latest/feed/$', LatestArticlesFeed()),
    url(r'author/(?P<slug>\w+)/$', cache_page(settings.CACHE_TIME)(ArticleAuthorListView.as_view()),
        name='author-list'),
    url(r'search/', SearchView.as_view(), name='search'),
    url(r'(?P<slug>[\w-]+)/$', cache_page(settings.CACHE_TIME)(ArticleDetailView.as_view()), name='detail'),
]
