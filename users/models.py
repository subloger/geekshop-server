from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta

# Create your models here.


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() +
                                                  timedelta(hours=48)))

    def save_delete(self):
        self.is_active = False
        self.save()

    def is_activation_key_expired(self):
        try:
            if now() <= self.activation_key_expires:
                return False
            else:
                return True
        except Exception as err:
            print(err)


class ShopUser(models.Model):
    MALE = 'M'
    FEMALE ='W'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )

    user = models.OneToOneField(User, unique=True, null=False, db_index=True,
                                on_delete=models.CASCADE)
    about_me = models.TextField(verbose_name='О себе', max_length=512,
                                blank=True)
    gender = models.CharField(verbose_name='Пол', max_length=1,
                              choices=GENDER_CHOICES, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUser.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.shopuser.save()