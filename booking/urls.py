from django.urls import path
from .views import BookingListCreateView,RoomView
# RoomListCreateView


urlpatterns = [
    path('bookings/',BookingListCreateView.as_view()),
    path('listRoom/',RoomView.as_view())
    
]
