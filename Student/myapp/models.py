from django.db import models

class student(models.Model):
    name = models.CharField(max_length=100)
    email = models.TextField()
    pno = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    bgroup = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)  


class Patient_ob(models.Model):
    observations = models.TextField()
    
