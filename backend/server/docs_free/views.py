from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import UserLog

class UserLogList(ListView):
    model = UserLog
    ordering = '-time_in'
    template_name       = 'docs_free/userlog_list.html'
    context_object_name = 'userlog_list'
    paginate_by = 5

class UserLogDetail(DetailView):
    model = UserLog
    template_name       = 'docs_free/userlog_detail.html'
    context_object_name = 'userlog_detail'
 
