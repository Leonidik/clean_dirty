from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from datetime import datetime

class UserLog(models.Model):
    time_in = models.DateTimeField(auto_now_add = True)
    user    = models.ForeignKey(User, on_delete = models.CASCADE,)
    user_ip = models.CharField(max_length=200)     
    image   = models.ImageField(upload_to='images/') 
    resp    = models.CharField(max_length=200)
 
    def __str__(self): 
        return self.user.username 

    def get_absolute_url(self):
        return f'/docs_work/{self.pk}/'   

@property
def image_url(self):
    if self.image and hasattr(self.image, 'url'):
        return self.image.url


