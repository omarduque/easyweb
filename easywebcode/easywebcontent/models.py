from django.db import models

# Create your models here.


class Curated(models.Model):
    title = models.CharField(max_length=600)
    category = models.CharField(max_length=200)
    name = models.CharField(max_length=400)
    tool_url = models.CharField(max_length=400)