from django.contrib import admin
from .models import Profile, Store, InventoryItem, Wishlist, Request, Delivery,Rating

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'points', 'is_online')
    list_filter = ('is_online',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Store)
admin.site.register(InventoryItem)
admin.site.register(Wishlist)
admin.site.register(Request)
admin.site.register(Delivery)
admin.site.register(Rating)
