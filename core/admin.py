from django.contrib import admin
from .models import Profile, Store, InventoryItem, Wishlist, Request, Delivery,Rating

admin.site.register(Profile)
admin.site.register(Store)
admin.site.register(InventoryItem)
admin.site.register(Wishlist)
admin.site.register(Request)
admin.site.register(Delivery)
admin.site.register(Rating)

