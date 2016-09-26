from django.db import models
from django.contrib import admin
from django import forms



# Create your models here.


class Challenge(models.Model):
    """
    The Challenge model is a collection of data for each challenge the user can complete.
    Challenges are simple CTF-esque problems where a user has to find a text string and evaluate it against the
    stored result.
    """

    # This section defines the different categories of problems
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

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    attachments = models.FileField(blank=True, null=True, upload_to='media')
    points = models.IntegerField()
    category = models.CharField(
        max_length=2,
        choices=CHALLENGE_CATEGORIES
    )
    key_hash = models.CharField(max_length=32)

class ChallengeAdmin(admin.ModelAdmin):

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(ChallengeAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield

    class Meta():
        fields = '__all__'

class Score(models.Model):
    value = models.IntegerField(default=0)
    category = models.CharField(
        max_length=2,
        choices=Challenge.CHALLENGE_CATEGORIES
    )
