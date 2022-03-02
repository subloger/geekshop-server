from django.shortcuts import render

from users.models import User

# Create your views here.

def index(request):
    context = {'title': 'GeekShop - Админ'}
    return render(request, 'admins/index.html', context)


# Read controller
def admin_users(request):
    users = User.objects.all()
    context = {'title': 'GeekShop - Админ', 'users': users}
    return render(request, 'admins/admin-users-read.html', context)