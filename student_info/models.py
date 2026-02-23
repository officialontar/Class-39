from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    tel = models.CharField(max_length=15)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to='students/', null=True, blank=True)
    country = models.CharField(max_length=50)
    message = models.TextField(max_length=300)