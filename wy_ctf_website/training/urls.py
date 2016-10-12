from __future__ import absolute_import, unicode_literals

from django.conf.urls import url, include

from wy_ctf_website.training import views

urlpatterns = [
    url(
        regex=r'(?P<category>[A-Z]{2})',
        view=views.ChallengeListView.as_view(),
        name='challenge-list'
    ),
    url(
        regex=r'challenge/(?P<pk>[0-9])',
        view=views.ChallengeView.as_view(),
        name='challenge'
    ),
    url(
        regex=r'terminal',
        view=views.TerminalRegistration.as_view(),
        name='terminal'
    ),
    url(
        r'web/',
        include('wy_ctf_website.training.web_urls', namespace='web')

    )
]
