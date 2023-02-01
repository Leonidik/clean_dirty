from django.shortcuts import render

# Create your views here.

# Подключение стандартной формы для регистрации
from django.contrib.auth.forms import UserCreationForm
 

# Функция регистрации
def registr(request):
    # Массив для передачи данных шаблоны
    data = {}
    # Проверка что есть запрос POST
    if request.method == 'POST':
        # Создаём форму
        form = UserCreationForm(request.POST)
        # Валидация данных из формы
        print('form.is_valid():', form.is_valid())
        if form.is_valid():
            # Сохраняем пользователя
            form.save()
            # Передача формы к рендару
            data['form'] = form
            # Передача надписи, если прошло всё успешно
            data['res'] = "Всё прошло успешно"
            # Рендаринг страницы
            return render(request, 'users/logup.html', data)
    else: # Иначе
        # Создаём форму
        form = UserCreationForm()
        # Передаём форму для рендеринга
        data['form'] = form
        # Рендаринг страницы
        return render(request, 'users/logup.html', data)



