from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    body=models.CharField(max_length=1000000)
    created_at =models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

class Users(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.username

