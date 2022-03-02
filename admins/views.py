from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from users.models import User
from admins.forms import UserAdminRegistrationForm

# Create your views here.

def index(request):
    context = {'title': 'GeekShop - Админ'}
    return render(request, 'admins/index.html', context)


# Read controller
def admin_users(request):
    users = User.objects.all()
    context = {'title': 'GeekShop - Админ', 'users': users}
    return render(request, 'admins/admin-users-read.html', context)


# Create controller
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminRegistrationForm()
    context = {'title': 'GeekShop - Админ', 'form': form}
    return render(request, 'admins/admin-users-create.html', context)