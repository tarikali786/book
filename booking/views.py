from rest_framework import generics, status
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from .models import Booking,Room
from .serializers import BookingSerializer,RoomSerializer
from rest_framework.views import APIView
class BookingListCreateView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    def get_queryset(self):
        return Booking.objects.all()
    def post(self, request, *args, **kwargs):
        serializer =BookingSerializer(data = request.data) 
        if serializer.is_valid():
            room = serializer.validated_data['room']
            start_time = serializer.validated_data['start_time']
            end_time = serializer.validated_data['end_time']
            capacity = serializer.validated_data['capacity']
            if Booking.objects.filter(room=room, start_time__lte=end_time, end_time__gte=start_time).exists():
                return Response({'message': 'The room is already booked for this time'}, status=status.HTTP_400_BAD_REQUEST)
            if start_time.date() != end_time.date() or \
                start_time.minute % 15 != 0 or \
                end_time.minute % 15 != 0 or \
                start_time.hour < 0 or \
                start_time.hour >= 24 or \
                end_time.hour < 0 or \
                end_time.hour >= 24 or \
                end_time > start_time.replace(hour=23, minute=45):
                return Response({'error': 'Invalid booking time'}, status=status.HTTP_400_BAD_REQUEST)
          
            if capacity > 0 and capacity <= 3 and room.id == 1:
                booking = Booking(room=room, start_time=start_time, end_time=end_time,capacity=capacity)
                serializer = BookingSerializer(booking, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'data':serializer.data,'message':"contact room is book this time "}, status=status.HTTP_201_CREATED)
                else:
                    return Response({'error': 'data invalid'}, status=status.HTTP_400_BAD_REQUEST)
            elif int(capacity) > 3 and int(capacity) <= 7 and room == 2:
                booking = Booking(room=room, start_time=start_time, end_time=end_time,capacity=capacity)
                serializer = BookingSerializer(booking, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'data':serializer.data,'message':"contact room is book this time "}, status=status.HTTP_201_CREATED)
                else:
                    return Response({'error': 'data invalid'}, status=status.HTTP_400_BAD_REQUEST)
            elif int(capacity) > 7 and int(capacity) <= 20 and room == 3:
                booking = Booking(room=room, start_time=start_time, end_time=end_time,capacity=capacity)
                serializer = BookingSerializer(booking, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'data':serializer.data,'message':"contact room is book this time "}, status=status.HTTP_201_CREATED)
                else:
                    return Response({'error': 'data invalid'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'capacity is high  try  another room'}, status=status.HTTP_400_BAD_REQUEST)



            
class RoomView(APIView):
    def get(self, request):
        book = Room.objects.all()
        serializer = RoomSerializer(book, many=True)
        return Response(serializer.data)
            
            
            
