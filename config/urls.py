# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^users/', include('wy_ctf_website.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here
    url(r'^training/', include('wy_ctf_website.training.urls', namespace='training')),
    url(r'^tools/', include('wy_ctf_website.tools.urls', namespace='tools')),
    url(r'^willchan/', include('wy_ctf_website.willchan.urls', namespace='willchan')),

    url(r'^docmo/', TemplateView.as_view(template_name='training/docmo.html'), name='docmo'),

    # OK SO I'M BEING A BAD BOY AND RUNNING MY LATEX BOT OFF OF THE SERVER SUE ME
    url(r'^latex/', include('wy_ctf_website.latex.urls', namespace='latex'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
