from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    usable_password = None
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    fieldset = fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('listPokemon',)}),
    )
    list_display = ["email", "username", "listPokemon"]

admin.site.register(CustomUser, CustomUserAdmin)