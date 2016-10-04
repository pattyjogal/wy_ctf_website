from django.contrib import admin

# Register your models here.
from wy_ctf_website.tools.models import Tool, ToolAdmin

admin.site.register(Tool, ToolAdmin)
