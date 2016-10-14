from django.contrib import admin
from .models import Challenge, ChallengeAdmin, Solution, Score

# Register your models here.

admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(Solution)
admin.site.register(Score)
