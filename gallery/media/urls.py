# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include

import media.views as media_views

uuid_pattern = r'(?P<uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})'

urlpatterns = [
    url('^collection/{}/$'.format(uuid_pattern), media_views.collection, name="collection"),
    url('^item/{}/$'.format(uuid_pattern), media_views.item, name="item"),
    url('^share/{}/$'.format(uuid_pattern), media_views.share, name="share"),
]
