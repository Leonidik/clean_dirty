from django.apps import AppConfig
import torch

class ApiConfig(AppConfig):
    name = 'rest_api'
    
    path = 'net_models/resnet_34.pth'
    model = torch.load(path)
    
    mean = [0.485, 0.456, 0.406]
    std  = [0.229, 0.224, 0.225]



