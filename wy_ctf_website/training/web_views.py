from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView

from config.settings.common import env

class InspectProblem(TemplateView):
    template_name = 'training/web/inspectme.html'

    def post(self, request, *args, **kwargs):
        if request.POST['password'] == env('INSPECT_PASSWORD'):
            messages.success(request, "Nicely done! Your flag is %s" % env('INSPECT_FLAG'))
            return redirect(reverse('training:web:inspect'))
        else:
            messages.error(request, "How DARE you try to hack me!")
            return redirect(reverse('training:web:inspect'))



