from django.shortcuts import render

# Create your views here.
from .apps import ApiConfig 

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

import numpy as np
import cv2
from net_models.resnet_34 import resnet_34

from docs_work.models import UserLog

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def view_api(request):
    print('---------------------------------')     
    print('LOGNAME    : ', request.META['LOGNAME'])      
    print('SERVER_NAME: ', request.META['SERVER_NAME'])
    print('REMOTE_ADDR: ', request.META['REMOTE_ADDR'])   
    print('HTTP_HOST  : ', request.META['HTTP_HOST'])
    print('REMOTE_ADDR: ', request.META['REMOTE_ADDR'])
    print('HTTP_AUTHORIZATION: ', request.META['HTTP_AUTHORIZATION'])    
#    print(request.META)          
    print('-------------------------------------') 
    f = request.data['image'] 
#    f = request.data.get('image')
    image = np.frombuffer(f.read(), 'uint8')
    image = cv2.imdecode(image, 1)
    print('file name  :  ', f.name)    
    print('image shape:', image.shape)

    tmp = resnet_34(image)   
    user_ip = request.META['REMOTE_ADDR']     
    user_id = request.user.id

    print('username:', request.user) 
    print('user_id :', user_id)
    print('user_ip :', user_ip)
         
#    UserLog.objects.create(user_ip=user_ip, user_id=user_id, image=f, resp=tmp) 

    return Response(tmp)
    
    


