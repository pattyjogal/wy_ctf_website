from django.db import models

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    body = models.CharField(max_length=512)
    picture = models.CharField(max_length=100, blank=True, null=True)
    admin = models.BooleanField(default=False)
