# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from wy_ctf_website.training.models import Challenge
from .models import User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(UserDetailView, self).get_context_data(**kwargs)
        # Give totals for all scores
        context['crypto_total'] = self.total_points(Challenge.CRYPTOGRAPHY)
        context['algo_total'] = self.total_points(Challenge.ALGORITHMS)
        context['web_total'] = self.total_points(Challenge.WEB)
        context['pwn_total'] = self.total_points(Challenge.PWNING)
        context['forensics_total'] = self.total_points(Challenge.FORENSICS)
        context['linux_total'] = self.total_points(Challenge.LINUX)
        context['rev_eng_total'] = self.total_points(Challenge.REVERSE_ENGINEERING)

        # Now pass the user's categorical scores in:
        context['user_crypto'] = self.user_score(Challenge.CRYPTOGRAPHY)
        context['user_algo'] = self.user_score(Challenge.ALGORITHMS)
        context['user_web'] = self.user_score(Challenge.WEB)
        context['user_pwn'] = self.user_score(Challenge.PWNING)
        context['user_forensics'] = self.user_score(Challenge.FORENSICS)
        context['user_linux'] = self.user_score(Challenge.LINUX)
        context['user_rev_eng'] = self.user_score(Challenge.REVERSE_ENGINEERING)

        return context

    def total_points(self, category):
        points_total = 0
        for challenge in Challenge.objects.filter(category=category):
            points_total += challenge.points
        return  points_total

    def user_score(self, category):
        points_total = 0
        for score in self.request.user.score.filter(category=category):
            points_total += score.value
        return points_total

    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'