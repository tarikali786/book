# Register your models here.
from django.contrib import admin
from .models import Booking,Room
# Register your models here.

admin.site.register(Booking)

class RoomAdmin(admin.ModelAdmin):
    list_display=['id','name']
admin.site.register(Room,RoomAdmin)
