from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm

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


# Update controller
def admin_users_update(request, pk):
    selected_user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {'title': 'Geekshop - Admin', 'form': form, 'selected_user': selected_user}
    return render(request, 'admins/admin-users-update-delete.html', context)


# Delete comtroller
def admin_users_delete(request, pk):
    user = User.objects.get(id=pk)
    user.save_delete()
    return HttpResponseRedirect(reverse('admin_staff:admin_users'))