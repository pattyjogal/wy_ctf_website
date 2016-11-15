from django.contrib import admin
from django import forms
from django.db import models
from django.utils.text import capfirst
from django.core import exceptions
# Create your models here.
from django.forms import forms, Textarea, MultipleChoiceField, CheckboxSelectMultiple

class Platform(models.Model):
    name = models.CharField(max_length=32)
    icon = models.CharField(max_length=64)
    def __str__(self):
        return self.name


class Tool(models.Model):

    FORENSICS = 'FR'
    CRYPTOGRAPHY = 'CR'
    LINUX = 'LX'
    ALGORITHMS = 'AL'
    WEB = 'WB'
    REVERSE_ENGINEERING = 'RE'
    PWNING = 'PW'

    CHALLENGE_CATEGORIES = (
        (FORENSICS, "Forensics"),
        (CRYPTOGRAPHY, "Cryptography"),
        (LINUX, "Linux"),
        (ALGORITHMS, "Algorithms"),
        (WEB, "Web"),
        (REVERSE_ENGINEERING, "Reverse Engineering"),
        (PWNING, "Pwning"),
    )



    name = models.CharField(max_length=255)
    category = models.CharField(
        max_length=2,
        choices=CHALLENGE_CATEGORIES
    )
    description = models.CharField(max_length=999)
    author = models.CharField(max_length=255)
    platform = models.ManyToManyField(Platform)
    program = models.CharField()
    documentation = models.CharField()

class ToolAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(ToolAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description':
            formfield.widget = Textarea(attrs=formfield.widget.attrs)
            return formfield
        return formfield
    class Meta():
        fields = '__all__'

