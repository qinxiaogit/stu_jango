from django.db import models

# Create your models here.
class Article(models.Model):
    status_choices=(
        ('d','Draft'),
        ('p','Pubished')
    )

    title = models.CharField('标题',max_length=200)
    body  = models.TextField('正文')
    create_time = models.DateTimeField('创建时间',auto_now_add=True);
    last_modified_time = models.DateTimeField('最后修改时间',auto_now=True)

    status = models.CharField('状态',max_length=1
                              ,choices=status_choices)

    abstrct = models.CharField('摘要',max_length=50
                               ,blank=True,null=True
                               ,help_text="可选，如若为空将摘取正文的前50个字符")

    views = models.PositiveIntegerField('浏览量',default=0)
    topped = models.BooleanField('置顶',default=False)

    category = models.ForeignKey('Category',verbose_name="分类"
                                 ,null=True,on_delete=models.SET_NULL
                                 )

    def __str__(self):
        return self.title

    class Meta:
        ordering =['-last_modified_time'];

"""
    文章分类
"""
class Category(models.Model):
    name = models.CharField('分类名称',max_length=50)
    create_time = models.DateTimeField('添加时间',auto_now_add=True);
    last_modified_time = models.DateTimeField('最后修改时间',auto_now=True)

    def __str__(self):
        return self.name

"""
    文章评论
"""
class Comment(models.Model):
    title = models.CharField('标题',max_length=20)
    create_time = models.DateTimeField('添加时间',auto_now_add=True);
    # context = models.
