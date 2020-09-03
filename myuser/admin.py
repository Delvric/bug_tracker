from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from myuser.models import MyUser


class MyUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom Field Heading',
            {
                'fields': (
                    'position',
                ),
            },
        ),
    )


admin.site.register(MyUser, MyUserAdmin)
