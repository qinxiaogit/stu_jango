from django.db import models

# Create your models here.

# class Person(models.Model):
#     first_name = models.charField(max_length=30)
#     last_name = models.CharField(max_length=30)

'''
# 多对多关系(manyToMany)
class Topping(models.Model):
    pass

class Pizza(models.Model):
    tippings = models.ManyToMany(Topping)
'''

"""
#多模型关联

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person,through="Membership")

    def __str__(self):
        return self.name;

    def __unicode__(self):
        return self.name

class Membership(models.Model):
    person = models.Foreignkey(Person)
    group = models.Foreignkey(Group)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

"""




