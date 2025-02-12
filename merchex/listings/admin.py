from django.contrib import admin

from listings.models import Band, Listings

admin.site.register(Band)

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'band')  
