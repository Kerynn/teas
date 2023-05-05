from django.db import models

class Tea(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    temperature = models.IntegerField()
    brew_time = models.TextField()

    def __str__(self):
      return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=200)

    def __str__(self):
      return self.first_name + " " + self.last_name