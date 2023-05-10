from django.db import models

class Tea(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    temperature = models.IntegerField()
    brew_time = models.TextField()
    tea_subscription = models.ManyToManyField('Customer', through='Subscription')

    def __str__(self):
      return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    customer_subscription = models.ManyToManyField('Tea', through='Subscription')

    def __str__(self):
      return self.first_name + " " + self.last_name

class Subscription(models.Model):
    tea = models.ForeignKey(Tea, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=200)
    frequency = models.CharField(max_length=200)