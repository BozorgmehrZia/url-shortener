from django.db import models

# Create your models here.
class Shortener(models.Model):
    created = models.DateTimeField()
    long_url = models.URLField()
    short_url = models.CharField(unique=True, max_length=6)