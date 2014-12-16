from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from cards import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexView.as_view(), name = 'index'),

    url(r'^card/(?P<slug>\w+)/$', views.view, name = 'view'),
    url(r'^create/(?P<template_id>[0-9]+)/$', views.create, name = 'create'),
    url(r'^add/$', views.add, name = 'add'),
    url(r'^image/$', views.image, name = 'image'),
    url(r'^artists/', views.IndexArtistView.as_view(), name = 'index_artist'),
    #url(r'^artist/(?P<artist_id>[0-9]+)/$', views.artist, name = 'artist'),
)

urlpatterns += staticfiles_urlpatterns()
