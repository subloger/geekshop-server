from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm


# Create your views here.
@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'GeekShop - Админ'}
    return render(request, 'admins/index.html', context)


# Read controller
class UserAdminListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserAdminListView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'GeekShop - Admin'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserAdminListView, self).dispatch(request, *args, **kwargs)


# Create controller
class UserAdminCreateView(CreateView):
    model = User
    form_class = UserAdminRegistrationForm
    template_name = 'admins/admin-users-create.html'
    success_url = reverse_lazy('admin_staff:admin_users')


# Update controller
class UserAdminUpdateView(UpdateView):
    model = User
    form_class = UserAdminProfileForm
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')


# Delete controller
class UserAdminDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.save_delete()
        return HttpResponseRedirect(self.success_url)
