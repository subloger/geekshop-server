from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from baskets.models import Basket, User
# Create your views here.


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'title': 'GeekShop - Авторизация', 'form': form}
    return render(request, 'users/login.html', context)


def registration(request):

    def send_verify_link(user):
        verify_link = reverse('users:verify', args=[user.email, user.activation_key])
        subject = f'Для активации пользователя {user.username} пройдите по ссылке'
        message = f'Для подтверждения учетной записи {user.username} на портале\n' \
                  f'{settings.DOMAIN_NAME} перейдите по ссылке {settings.DOMAIN_NAME}{verify_link}'
        return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            usr = form.new_save()
            if send_verify_link(usr):
                messages.success(request, 'Сообщение подтверждения отправлено')
                return HttpResponseRedirect(reverse('users:login'))
            else:
                messages.error(request, 'Ошибка отправки сообщения')
                return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'title': 'GeekShop - Регистрация', 'form': form}
    return render(request, 'users/registration.html', context)


def verify(request, email, activate_key):
    try:
        user = User.objects.get(email=email)
        if user.activation_key == activate_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save(update_fields=['activation_key', 'activation_key_expires', 'is_active'])
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request, 'users/verification.html')
        else:
            return render(request, 'users/verification.html')
    except Exception as err:
        print(err)
        #return HttpResponseRedirect(reverse('products:index'))


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'title': 'GeekShop - Профиль',
        'form': form,
        'baskets': Basket.objects.filter(user=request.user),
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
