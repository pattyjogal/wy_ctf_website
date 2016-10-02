from django.core.urlresolvers import reverse
from django.contrib import messages

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import Context
from django.views.generic import DetailView, ListView


from wy_ctf_website.training.models import Challenge, Score

import hashlib

class ChallengeListView(ListView):
    model = Challenge
    def get_queryset(self):
        print(self.kwargs['category'])
        print(Challenge.objects.filter(category=self.kwargs['category']))
        return Challenge.objects.filter(category=self.kwargs['category'])

class ChallengeView(DetailView):
    model = Challenge
    template_name = 'training/challenge_detail.html'
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Let's reward the user if they got it right!
        user_answer = request.POST['answer']
        user_answer_hash = hashlib.md5(user_answer.encode('utf-8')).hexdigest()

        if self.hash_validator(user_answer_hash) and self.get_object() not in request.user.completed_challenges.all():
            score = Score(value=self.get_object().points, category=self.get_object().category)
            score.save()
            request.user.completed_challenges.add(self.get_object())
            request.user.score.add(score)
            messages.add_message(request, messages.SUCCESS, "You earned %i points!" % score.value)
            con = self.get_context_data(object=self.get_object())
            self.get_object().solves += 1
            return render(request, self.template_name, con)
        else:
            points_total = 0
            for score in request.user.score.all():
                points_total += score.value
            if self.get_object() in request.user.completed_challenges.all():
                messages.add_message(request, messages.WARNING, "Hey, you already got this one!")
                con = self.get_context_data(object=self.get_object())
                return render(request, self.template_name, con)
            else:
                messages.add_message(request, messages.ERROR, "Nope, not quite correct. Try again!")
                con = self.get_context_data(object=self.get_object())
                return render(request, self.template_name, con)
    def hash_validator(self, user_response):
        challenge_object_hashes = self.get_object().key_hashes.all()
        for sol in challenge_object_hashes:
            if user_response == sol.hash:
                return True
        return False

