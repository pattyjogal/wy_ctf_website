from django.contrib import admin
from .models import Challenge, ChallengeAdmin, Solution

# Register your models here.

admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(Solution)
