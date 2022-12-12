from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pizza(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text 

class Entry(models.Model): 
    item = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField(max_length=100)
    #date_added = models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text
    #def __str__(self):
    #    return f"{self.text[:50]}...."