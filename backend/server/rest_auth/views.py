from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def view_auth(request):
    print('---------------------------------')
    username = request.POST['username']
    password = request.POST['password']
    
    try:
        user = User.objects.get(username=username)
        if check_password(password, user.password):
            token = Token.objects.get(user=user)    
            
            print(f'User {user} already has token')
            print(str(token))
            response = {'text' : f'User {user} already has token',      
                        'token': str(token)}
        else:
            print(f'User {user} enter wrong password')
            response = {'text' : f'User {user} enter wrong password',
                        'token':''}            
        return Response(response)
        
    except:
        User.objects.create_user(username=username, password=password)
        user  = User.objects.get(username=username)
        token = Token.objects.create(user=user) 
        print(f'User {user} is regisged and recieved his token')
        print(str(token))
        response = {'text' : f'User {user} is regisged and recieved his token',
                    'token': str(token)}
        return Response(response)  
        
        
              


