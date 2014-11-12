from django.conf.urls import patterns, include, url
from django.contrib import admin
from cards import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name = 'index'),
    url(r'^card/(?P<hashed_id>\w+)/$', views.view, name = 'view'),
    url(r'^create/(?P<template_id>[0-9]+)/$', views.create, name = 'create'),
    url(r'^share/(?P<hashed_id>\w+)/$', views.share, name = 'share'),
)
