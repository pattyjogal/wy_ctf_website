from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from config.settings.common import MESSENGER_VALIDATION_TOKEN
# Create your views here.
from django.views.generic import View


def latex_webhook(request):
    if request.method == 'GET':
        if (request['hub.mode'] == 'subscribe' and request['hub.verify_token'] == MESSENGER_VALIDATION_TOKEN):
            return HttpResponse(request['hub.challenge'])
        else:
            return HttpResponseForbidden()
