from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Person(User):
    

    class Meta:
        proxy = True


class After10(models.Model):
    question=models.CharField(max_length=150,unique=True)

class After12Arts(models.Model):
    question=models.CharField(max_length=150,unique=True)

class After12Commerce(models.Model):
    question=models.CharField(max_length=150,unique=True)

class After12Science(models.Model):
    question=models.CharField(max_length=150,unique=True)


class Caste(models.Model):
    caste=models.CharField(max_length=150,unique=True)

    def __str__(self):
        return self.caste

class Standard(models.Model):
    std=models.CharField(max_length=150,unique=True)

    def __str__(self):
        return self.std

class Board(models.Model):
    board=models.CharField(max_length=150,unique=True)

    def __str__(self):
        return self.board
