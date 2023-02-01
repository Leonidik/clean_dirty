# URLs for docs_free

from django.urls import path
from .views import UserLogList, UserLogDetail 

urlpatterns = [
   path('',          UserLogList.as_view(),   name='userlog_list'),
   path('<int:pk>/', UserLogDetail.as_view(), name='userlog_detail'), 
      
#   path('docs_free/search/',           PostSearch.as_view(), name='post_search'),
#   path('docs_free/search/<int:pk>/',  PostDetail.as_view(), name='post_detail'),   
   
]

