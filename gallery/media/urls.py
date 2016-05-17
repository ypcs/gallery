# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'collections', views.CollectionViewSet)
router.register(r'items', views.ItemViewSet)

uuid_pattern = r'(?P<uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})'

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^collection/{}/$'.format(uuid_pattern), views.collection, name="collection"),
    url(r'^item/{}/$'.format(uuid_pattern), views.item, name="item"),
    url(r'^share/{}/$'.format(uuid_pattern), views.share, name="share"),
]
