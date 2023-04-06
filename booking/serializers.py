from .models import Room, Booking
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from .models import Room, Booking


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields =['id','room','start_time','end_time','capacity']
