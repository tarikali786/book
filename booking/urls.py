from django.urls import path
from .views import BookingListCreateView
# RoomListCreateView


urlpatterns = [
    path('bookings/',BookingListCreateView.as_view()),
    # path('listRoom/',RoomListCreateView.as_view())
    
]
