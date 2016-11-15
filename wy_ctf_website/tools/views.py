from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from wy_ctf_website.tools.models import Tool


class ToolsList(ListView):
    model = Tool
    template_name = 'tools/tools-list.html'


