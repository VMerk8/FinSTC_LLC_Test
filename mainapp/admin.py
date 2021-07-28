from django.contrib import admin

from .models import Dealer, Car, Manufacturer

admin.site.register(Dealer)
admin.site.register(Car)
admin.site.register(Manufacturer)
