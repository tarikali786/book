from rest_framework import generics, status
from rest_framework.response import Response

from .models import Booking
from .serializers import BookingSerializer

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
                return Response({'message': 'The room is already booked for this time'}, 
                                status=status.HTTP_400_BAD_REQUEST)

            if int(capacity) > 0 and int(capacity) <= 3 and room == 1:
                return self.create(request, *args, **kwargs)
            elif int(capacity) > 3 and int(capacity) <= 7 and room == 2:
                return self.create(request, *args, **kwargs)
            elif int(capacity) > 7 and int(capacity) <= 20 and room == 3:
                return self.create(request, *args, **kwargs)
            else:
                return Response({'error': 'try another room'}, status=status.HTTP_400_BAD_REQUEST)
            
        else:
                return Response({'error': 'data not valid '}, status=status.HTTP_400_BAD_REQUEST)
            
