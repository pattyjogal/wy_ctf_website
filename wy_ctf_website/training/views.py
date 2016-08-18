from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
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

    def post(self, request, *args, **kwargs):
        # Let's reward the user if they got it right!
        user_answer = request.POST['answer']
        correct_answer_hash = self.get_object().key_hash
        user_answer_hash = hashlib.md5(user_answer.encode('utf-8')).hexdigest()
        if (user_answer_hash == correct_answer_hash) and self.get_object() not in request.user.completed_challenges.all():
            score = Score(value=self.get_object().points, category=self.get_object().category)
            score.save()
            request.user.completed_challenges.add(self.get_object())
            request.user.score.add(score)
            return HttpResponse("You got " + str(score.value) + " points!")
        else:
            points_total = 0
            for score in request.user.score.all():
                points_total += score.value
            return HttpResponse("Bad boy/girl! Trying to get more points, for shame.<br>You have " + str(points_total) +  " points")




