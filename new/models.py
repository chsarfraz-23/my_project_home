from django.db import models

# Create your models here.

class NewModel(models.Model):
    name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=300)


class MyModel(models.Model):
    name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=300)

class Sarfraz(models.Model):
    name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=300)
