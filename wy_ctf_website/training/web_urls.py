from __future__ import absolute_import, unicode_literals

from django.conf.urls import url, include

from wy_ctf_website.training import views
from wy_ctf_website.training.web_views import InspectProblem

urlpatterns = [
    url(regex=r'01',
        view=InspectProblem.as_view(),
        name='inspect'
        )
    ]
