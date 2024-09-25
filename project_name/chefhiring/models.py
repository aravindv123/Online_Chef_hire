from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Optional profile picture
    phone_number = models.CharField(max_length=15, blank=True)  # Optional phone number
    specialties = models.CharField(max_length=100, blank=True)  # Optional specialties for chefs

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['user__username']  # Optional: Order profiles by username
class Chef(models.Model):
    username = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)