from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Article,Category
# import markdown2
from django.views.generic import ListView,DetailView

from django.utils import timezone

class IndexView(ListView):
    template_name  = "blog/index.html"

    # 属性用于给上下文变量取名（在模板中使用该名字）
    context_object_name  = "article_list"

    """
    过滤数据，获取所有已发布文章，并且将内容转成markdown形式
    """

    def get_queryset(self):
        article_list = Article.objects.filter(status='p')
        # for article in article_list:
        #     article.body = markdown2.markdown(article.body,)
        return article_list

    """
        增加额外的数据，这里返回一个文章分类，以字典的形式
    """

    def get_content_data(self,**kwargs):
        kwargs['']=Article.objects.all().order_by('name')
        return super(IndexView, self).get_content_data(kwargs)


class ArticleDetailView(DetailView):
    model = Article
    pk_url_kwarg = 'article_id'
    template_name = 'blog/detail.html'
    context_object_name = 'aticle'

    def get_object(self,**kwargs):
        object = super(ArticleDetailView, self).get_object(**kwargs)
        # object['now'] = timezone.now()
        return object

