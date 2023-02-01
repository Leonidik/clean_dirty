# rest_auth URLs Configuration

from django.urls import path
from .views import view_auth
     
urlpatterns = [
   path('', view_auth),     
     
]




