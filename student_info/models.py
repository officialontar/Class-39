from django.db import models


class Student(models.Model):

    # ---------- GENDER CHOICES ----------
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    # ---------- COUNTRY CHOICES ----------
    COUNTRY_CHOICES = [
        ('usa', 'USA'),
        ('australia', 'Australia'),
        ('canada', 'Canada'),
    ]

    # ---------- BASIC INFO ----------
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    tel = models.CharField(max_length=15)
    dob = models.DateField()

    # ---------- CHOICES FIELD ----------
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    country = models.CharField(max_length=20, choices=COUNTRY_CHOICES)

    # ---------- IMAGE ----------
    profile_pic = models.ImageField(upload_to='students/', null=True, blank=True)

    # ---------- MESSAGE ----------
    message = models.TextField(max_length=300)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"