from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'title': 'GeekShop - Админ-панель'}
    return render(request, 'admins/index.html', context)