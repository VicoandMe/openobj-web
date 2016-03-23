from django.contrib import admin

# Register your models here.
from usercenter.models import UserAccount


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    pass
