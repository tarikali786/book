from django.db import models
from django.utils import timezone
import datetime
from django.core.exceptions import ValidationError
class Room(models.Model):
    name = models.CharField(max_length=200)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now,blank=True,null=True)
    end_time = models.DateTimeField(default=timezone.now,blank=True,null=True)
    capacity = models.IntegerField()
    
   