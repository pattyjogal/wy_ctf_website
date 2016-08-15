from django.db import models

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
    attachments = models.FileField()
    points = models.IntegerField()
    category = models.CharField(
        max_length=2,
        choices=CHALLENGE_CATEGORIES
    )
    key_hash = models.CharField(max_length=32)

