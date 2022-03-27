from django.core.management.base import BaseCommand

from users.models import User, ShopUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            users_profile = ShopUser.objects.create(user=user)
            users_profile.save()
