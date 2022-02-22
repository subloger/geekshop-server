from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages

from users.forms import UserLoginForm, UserRegistrationForm
# Create your views here.


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'title': 'GeekShop - Авторизация', 'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        print('print 1')
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            print('print 2')
            form.save()
            messages.success(request, 'Поздравляем! Регистрация прошла успешно.')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm
    context = {'title': 'GeekShop - Регистрация', 'form': form}
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {'title': 'GeekShop - Профиль'}
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
