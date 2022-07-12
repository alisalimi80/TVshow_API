from email.policy import default
from django.db import models


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self) :
        return self.name
  
class Serial(models.Model):
    name = models.CharField(max_length=120)
    imdb = models.FloatField(default=0)
    genre = models.ManyToManyField(Genre)
    description = models.TextField()
    publishdate = models.DateField(auto_now=False)
    country = models.CharField(max_length=120)
    director = models.CharField(max_length=120)
    def __str__(self):
        return self.name
    
class Cast(models.Model):
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    age = models.IntegerField(default=0)
    avatar = models.CharField(max_length=1000,null=True)
    serial = models.ForeignKey(Serial,on_delete=models.CASCADE,related_name='casts')
    def __str__(self) :
        return (self.name + " " + self.last_name)

class Image(models.Model):
    img = models.CharField(max_length=1000)
    serial = models.ForeignKey(Serial,on_delete=models.CASCADE,related_name='image')
    def __str__(self):
        return self.serial
