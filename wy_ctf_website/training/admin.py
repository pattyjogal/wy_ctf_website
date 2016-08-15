from django.contrib import admin
from .models import Challenge, ChallengeAdmin

# Register your models here.

admin.site.register(Challenge, ChallengeAdmin)
