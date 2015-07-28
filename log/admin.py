from django.contrib import admin

from .models import Entry, Plane, Trip, Airport

admin.site.register(Entry)
admin.site.register(Plane)
admin.site.register(Trip)
admin.site.register(Airport)