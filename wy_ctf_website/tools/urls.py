from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from wy_ctf_website.tools import views

urlpatterns = [
    url(
        regex=r'list',
        view=views.ToolsList.as_view(),
        name='tools-list'
    ),

]
