from django.contrib import admin
from django.urls import path, include,re_path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Conference Room')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('booking.urls')),
    re_path('api/doc/', schema_view),
    
    
]
