from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    is_online = models.BooleanField(default=False)

class Store(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    inventory = models.TextField()

class Wishlist (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.TextField()

class Request(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    accepted_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="deliveries")
    status = models.CharField(max_length=50, default="Pending")

class Recognition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recognitions")
    points = models.PositiveIntegerField()