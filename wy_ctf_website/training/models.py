from django.db import models
from django.contrib import admin
from django import forms
import requests


# Create your models here.
from config.settings.common import env


class Solution(models.Model):
    hash = models.CharField(max_length=32)

    def __str__(self):
        return str(self.hash)

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
    attachments = models.FileField(blank=True, null=True)
    points = models.IntegerField()
    category = models.CharField(
        max_length=2,
        choices=CHALLENGE_CATEGORIES
    )
    key_hashes = models.ManyToManyField(Solution)
    solves = models.IntegerField(default=0)
    lesson = models.BooleanField(default=False)
    will = models.BooleanField(default=False)

    def __str__(self):
        return (str(self.name))

def post_save_challenge(sender, instance, created, *args, **kwargs):
    if created:
        from requests.auth import HTTPBasicAuth
        r = requests.post(
            url='https://discordapp.com/api/channels/227554629741707274/messages',
            headers={
                'Authorization': 'Bot ' + env('DISCORD_TOKEN'),
                'User-Agent': 'ctf-bot (http://ctf.tips.club, v0.1)'
            },
            data={
                'content': "<@&228329733434114048> **New Problem:** {name}\nPoints: {points}\nCategory: {cat}"\
                .format(name=instance.name, points=instance.points, cat=instance.category)
            }
        )
        print(r.text)
        print(env('DISCORD_TOKEN'))

models.signals.post_save.connect(post_save_challenge, sender=Challenge)

class ChallengeAdmin(admin.ModelAdmin):

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(ChallengeAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield

    filter_horizontal = ['key_hashes',]

    class Meta():
        fields = '__all__'

class Score(models.Model):
    value = models.IntegerField(default=0)
    category = models.CharField(
        max_length=2,
        choices=Challenge.CHALLENGE_CATEGORIES
    )

