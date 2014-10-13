# -*- coding: gb18030-*-

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Tyraan_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    url(r'^admin/', include(admin.site.urls)),   
    
    url(r'^$', 'tyraan.views.blog_list',name='blog_list'), # 首页
    url(r'^bloglist/$','tyraan.views.blog_list',name='blog_list'),
    url(r'^article/(?P<slug>[-\w]+)/$','tyraan.views.blog_show',name='blog_article'), # 博文
    url(r'^category/(?P<slug>[-\w]+)/$','tyraan.views.category',name='blog_category'), # 分类
    url(r'^tag/(?P<id>\d+)/$','tyraan.views.tag',name='blog_tag'), # 标签
    
  
)