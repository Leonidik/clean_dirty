# coding=utf-8 

import requests
import matplotlib.pyplot as plt
from sys import argv
import time

print()
path = 'http://127.0.0.1:8000/'

# Получение токена / Регистрация и получение токена 
print('username:', argv[1])
print('password:', argv[2] )

request = {
   'username': 'ivanov',
   'password': 'ivanov' }
response = requests.post(
    url = path + 'auth/',
    data=request)

print(response)
print('Text   :', response.json()['text'])
token = 'Token ' + response.json()['token']
print('token  :', token)
print()

# Загрузка изображения
path_to_image = './data/' + argv[3]
image = open(path_to_image, 'rb')
print('path to image:', image.name)

# Отправка изображения
resp = requests.post(
    url     = path + 'api_img/',
    headers = {'Authorization': token},
    files   = {'image': image})
image.close()

# Ответ сервера
print(resp)
print('This plate is', resp.text[1:-1])

# Вывод изображения на экран
image = plt.imread(path_to_image)
plt.imshow(image)
plt.pause(5)
plt.close('all')


