from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    gender= models.CharField(max_length=30)
    address= models.CharField(max_length=30)

class predict_weather(models.Model):

    Fid= models.CharField(max_length=300)
    LATITUDE= models.CharField(max_length=300)
    LONGITUDE= models.CharField(max_length=300)
    wdate= models.CharField(max_length=300)
    precipitation= models.CharField(max_length=300)
    temp_max= models.CharField(max_length=300)
    temp_min= models.CharField(max_length=300)
    wind= models.CharField(max_length=300)
    Prediction= models.CharField(max_length=300)

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



