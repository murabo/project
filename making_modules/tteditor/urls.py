# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('tteditor.views',
    url(r'^$', 'index', name='tteditor/index'),
    url(r'^keys_on_server/(?P<ttname>\w+)/(?P<page_number>\d+)/$', 'keys_on_server', name='tteditor/keys_on_server'),
    url(r'^edit/(?P<ttname>\w+)/(?P<keyname>.+)/(?P<mode>\w+)/$', 'edit', name='tteditor/edit'),
    url(r'^save/$', 'save', name='tteditor/save'),
    url(r'^save_done/(?P<ttname>\w+)/(?P<keyname>.+)/(?P<mode>\w+)/$', 'edit', name='tteditor/save_done', kwargs={'save_done':True}),
    url(r'^delete/$', 'delete', name='tteditor/delete'),
)

