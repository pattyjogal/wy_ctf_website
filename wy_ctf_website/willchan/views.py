from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from wy_ctf_website.willchan.models import Comment


class WillchanHome(ListView):
    model = Comment
    template_name = 'willchan/comment-list.html'

    def get_queryset(self):
        qs = Comment.objects.all()
        i = int(self.kwargs['page'])
        qs = qs[::-1]
        return qs[25 * (i - 1):(25 * i)]

    def post(self, request, *args, **kwargs):
        comment = Comment()
        name = request.POST['name']
        body = request.POST['body']
        picture = request.POST['picture']

        if name:
            comment.name = name
        comment.body = body

        if picture:
            comment.picture = picture

        comment.save()

        return HttpResponseRedirect("/willchan/1")

