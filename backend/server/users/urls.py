# users URL Configuration

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import registr

urlpatterns = [
    path('login/',  LoginView.as_view(template_name  = 'users/login.html'),  name='login'),
    path('logup/',  registr),   
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
]



#from django.contrib.auth.views import LoginView, LogoutView
#from .views import BaseRegisterView, upgrade_me, common_me

#urlpatterns = [
#    path('login/', 
#         LoginView.as_view(template_name = 'users/login.html'),
#         name='login'),
#    path('logout/', 
#         LogoutView.as_view(template_name = 'users/logout.html'),
#         name='logout'),
#    path('logup/', 
#         BaseRegisterView.as_view(template_name = 'users/logup.html'), 
#         name='logup'),               
#]



