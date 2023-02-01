import torch
from torchvision import transforms
from rest_api.apps import ApiConfig

def resnet_34(image):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Resize((224)),        
        transforms.CenterCrop((224)),     
        transforms.Normalize(mean=ApiConfig.mean, std=ApiConfig.std), ])
    
    image = transform(image).unsqueeze(0)
    print('tensor shape:', image.shape)

    y = ApiConfig.model(image)
    m = torch.argmax(y.data, dim=1).numpy()[0]
       
    if m == 1: resp = 'clean'
    else: resp = 'dirty'
    
    print('net response:', resp)
    return resp


