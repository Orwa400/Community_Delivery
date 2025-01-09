from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    points = models.PositiveIntegerField(default=0)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Store(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class InventoryItem(models.Model):
    store = models.ForeignKey(Store, related_name='inventory', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.store.name})"

class Wishlist (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(InventoryItem, related_name='wishlist')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Wishlist"

class Request(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests_made')
    items = models.ManyToManyField(InventoryItem, related_name='requests')
    created_at = models.DateTimeField(default=now)
    is_fulfilled = models.BooleanField(default=False)

    def __str__(self):
        return f"Request by {self.requester.username}"

class Delivery(models.Model):
    request = models.OneToOneField(Request, on_delete=models.CASCADE)
    wishmaster = models.ForeignKey(User, on_delete=models.CASCADE, related_name='deliveries_made')
    delivered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Delivery by {self.wishmaster.username} for {self.rquets}"
    

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings_recieved")
    given_by = models.ForeignKey(User, on_delete= models.CASCADE, related_name='ratings_given')
    stars = models.PositiveIntegerField()
    feedback = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.stars}, stars for {self.user.username} by {self.given_by.username}"
