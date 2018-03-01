from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url('article/(?P<article_id>\d+)$',views.ArticleDetailView.as_view(),name='detail'),
    url(r'category/(?P<category_id>\d+)$',views.CategoryDetailView.as_view(),name="category")
]