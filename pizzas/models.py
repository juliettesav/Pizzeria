from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)

    def __str__(self):
        return self.pizza_name

class Topping(models.Model): 
    item = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.TextField(max_length=100)

    def __str__(self):
        return self.topping_name

class Photo(models.Model):
    photo = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    photo_file = models.ImageField(null=True)

    #def __str__(self):
    #    return self.photo_file