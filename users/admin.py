from django.contrib import admin

from users.models import User
from baskets.admin import BasketAdminInLine

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdminInLine,)