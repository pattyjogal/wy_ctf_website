from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from wy_ctf_website.latex import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.latex_webhook,
        name='latex'
    ),

]
