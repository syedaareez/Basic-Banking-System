from django.db import models

# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField(max_length=225,blank=True)
    balance=models.CharField(max_length=25)
    def __str__(self):
        return self.name
    
class History(models.Model):
    sendfrom=models.CharField(max_length=25)
    sendto=models.CharField(max_length=25)
    amount=models.CharField(max_length=25)
    date = models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.sendfrom