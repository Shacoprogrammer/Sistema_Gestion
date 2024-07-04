from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario, Eventos

class CustomuserAdmin(UserAdmin):
    model = Usuario
    list_display = ['username', 'email', 'first_name', 'last_name', 'rol', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('rol',)}),
    )

    add_fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('rol',)}),
    )

admin.site.register(Usuario, CustomuserAdmin)
admin.site.register(Eventos)




admin.site.register(Eventos)


