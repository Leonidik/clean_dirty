from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView


from .models import UserLog
from .forms   import ImageForm
from datetime import datetime

import numpy as np
import cv2
from net_models.resnet_34 import resnet_34

class UserLogList(ListView):
    model = UserLog
    ordering = '-time_in'
    template_name       = 'docs_work/userlog_list.html'
    context_object_name = 'userlog_list'
    paginate_by = 5
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user) 

class UserLogDetail(DetailView):
    model = UserLog
    template_name       = 'docs_work/userlog_detail.html'
    context_object_name = 'userlog_detail'
 
class ImageCreate(CreateView):
    form_class = ImageForm
    model = UserLog
    template_name = 'docs_work/image_create.html' 
    
    def form_valid(self, form):
        userlog = form.save(commit=False)
        userlog.time_in = datetime.now()              
        # текущий зарегистрированный пользователь, который создает документ
        userlog.user_id = self.request.user.pk        
        userlog.user_ip = '0.0.0.0'

        f = userlog.image.open(mode='rb')
        image = np.frombuffer(f.read(), 'uint8')
        image = cv2.imdecode(image, 1)
        tmp = resnet_34(image)
        userlog.resp = tmp        
        return super().form_valid(form)
  

 
 
 
 
