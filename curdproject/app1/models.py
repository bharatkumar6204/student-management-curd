from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    roll=models.CharField(max_length=100, unique=True)
    email=models.EmailField(max_length=150, unique=True)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=15)
