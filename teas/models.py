from django.db import models

class Tea(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    temperature = models.IntegerField()
    brew_time = models.TextField()
