from django.contrib import admin
from .models import ImpUser


class ImpUserAdmin(admin.ModelAdmin):
    list_display = ("username", "second_name", "first_name", "patronymic", "operation_email", "private_email",
                    "phone_number", "add_phone_number")


admin.site.register(ImpUser, ImpUserAdmin)

