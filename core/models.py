from django.db import models

# Create your models here.

class After10(models.Model):
    question=models.CharField(max_length=150,unique=True)

class After12Arts(models.Model):
    question=models.CharField(max_length=150,unique=True)

class After12Commerce(models.Model):
    question=models.CharField(max_length=150,unique=True)

class After12Science(models.Model):
    question=models.CharField(max_length=150,unique=True)
