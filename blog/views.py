from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Article,Category
# import markdown2
from django.views.generic import ListView,DetailView

from django.utils import timezone

class IndexView(ListView):
    # template_name  = "blog/index.html"
    #
    # # 属性用于给上下文变量取名（在模板中使用该名字）
    # context_object_name  = "article_info"
    #
    # """
    # 过滤数据，获取所有已发布文章，并且将内容转成markdown形式
    # """
    #
    # def get_queryset(self):
    #     article_list = Article.objects.filter(status='p')
    #     # for article in article_list:
    #     #     article.body = markdown2.markdown(article.body,)
    #
    #     return article_list;
    #
    # """
    #     增加额外的数据，这里返回一个文章分类，以字典的形式
    # """
    #
    # def get_content_data(self,**kwargs):
    #     kwargs['ategory'] = Category.objects.all().order_by('name')
    #     return super(IndexView, self).get_content_data(kwargs)
    # 继承自ListView,用于展示一个列表

    template_name = "blog/index.html"
    # 指定需要渲染的模板

    context_object_name = "article_list"
    # 指定模板中需要使用的上下文对象的名字

    def get_queryset(self):
        #get_queryset 的作用已在第一篇中有介绍，不再赘述
        article_list = Article.objects.filter(status='p')
        # 注意在url里我们捕获了分类的id作为关键字参数（cate_id）传递给了CategoryView，传递的参数在kwargs属性中获取。
        # for article in article_list:
        #     article.body = markdown2.markdown(article.body, )
        return article_list

    # 给视图增加额外的数据
    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        # 增加一个category_list,用于在页面显示所有分类，按照名字排序
        return super(IndexView, self).get_context_data(**kwargs)

class ArticleDetailView(DetailView):
    model = Article
    pk_url_kwarg = 'article_id'
    template_name = 'blog/detail.html'
    context_object_name = 'aticle'

    def get_object(self,**kwargs):
        object = super(ArticleDetailView, self).get_object(**kwargs)
        return object



