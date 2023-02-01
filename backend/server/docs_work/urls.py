# URLs for docs_free

from django.urls import path
from .views import UserLogList, UserLogDetail, ImageCreate 

urlpatterns = [
   path('',          UserLogList.as_view(),   name='userlog_list'),
   path('<int:pk>/', UserLogDetail.as_view(), name='userlog_detail'),
   path('image/edit/', ImageCreate.as_view(),   name='userlog_list'),  
       
]

