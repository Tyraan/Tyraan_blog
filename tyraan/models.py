# -*- coding: gb18030-*-

from django.db import models
from django.db.models import permalink

# Create your models here.
class Category(models.Model): 

    name = models.CharField(max_length=10,verbose_name=u'����')
    slug = models.CharField(max_length=50,unique=True,verbose_name=u'Slug')

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return ('blog_category',None,{'slug':self.slug})

    class Meta:
        ordering = ['id']
        verbose_name_plural = verbose_name = u'����'

class Tag(models.Model): 

    tag_name = models.CharField(max_length=20,blank=True,verbose_name=u'����')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name=u'����ʱ��')

    def __unicode__(self):
        return self.tag_name

    class Meta:
        verbose_name_plural = verbose_name = u'��ǩ'

class Blog(models.Model): 

    caption = models.CharField(max_length=50,verbose_name=u'����')
    slug = models.SlugField(max_length=50,unique=True,verbose_name=u'Slug')
    tags = models.ManyToManyField(Tag,blank=True,verbose_name=u'��ǩ����')
    content = models.TextField(verbose_name=u'����')
    publish_time = models.DateTimeField(auto_now_add=True,verbose_name=u'����ʱ��')
    update_time = models.DateTimeField(auto_now=True,verbose_name=u'����ʱ��')
    counts = models.IntegerField(default=0,verbose_name=u'�Ķ���')
    category = models.ForeignKey(Category,verbose_name=u'����')

    def __unicode__(self):
        return u'%s %s' % (self.caption,self.publish_time)

    @permalink
    def get_absolute_url(self):
        return ('blog_article',None,{'slug':self.slug})

    class Meta:
        get_latest_by = 'publish_time'
        ordering = ['-id']
        verbose_name_plural = verbose_name = u'����'

class ClientInfo(models.Model):

    ip_address = models.CharField(max_length=20,verbose_name=u'IP��ַ')
    time = models.DateTimeField(auto_now=True,verbose_name=u'����ʱ��')

    def __unicode__(self):
        return u'%s %s' % (self.ip_address,self.time)

    class Meta:
        get_latest_by = 'time'
        ordering = ['-id']
        verbose_name_plural = verbose_name = u'����ʱ��'