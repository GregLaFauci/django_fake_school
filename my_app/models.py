from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=264, unique=True)
    subject = models.CharField(max_length=180)
