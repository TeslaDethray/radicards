from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns, include, url
from cards import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexView.as_view(), name = 'index'),

    url(r'^card/(?P<slug>\w+)/$', views.DetailView.as_view(), name = 'view'),
    url(r'^create/(?P<template_id>[0-9]+)/$', views.create, name = 'create'),
    url(r'^add/$', views.add, name = 'add'),
    url(r'^share/(?P<slug>\w+)/$', views.ResultsView.as_view(), name = 'share'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
    )
