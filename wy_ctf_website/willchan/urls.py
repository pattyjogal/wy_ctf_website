# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from wy_ctf_website.willchan.views import WillchanHome
from . import views

urlpatterns = [
    url(r'(?P<page>[0-9])', WillchanHome.as_view(), name='home')
]
