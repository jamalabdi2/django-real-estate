from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserCreationForm,CustomUserChangeForm

class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    ordering = ["email"]
    form = CustomUserChangeForm
    model = User
    list_display = ["pkid","id","email","username","first_name","last_name","is_staff","is_active"]
    list_display_links = ["id","email"]
    list_filter = ["email","username","first_name","last_name","is_staff","is_active"]
    fieldsets = (
        (
            _("Login Credentials"),{"fields":("email","password",),}
        ),
        (
            _("Personal Information"),
            {
                "fields":("username","first_name","last_name",),
            },
        ),
        (
            _("Permissions and Groups"),
            {
                "fields":("is_active","is_staff","is_superuser","groups","user_permission",),
            },
        ),
        (
            _("Important Dates"),
            {
                "fields":("last_login","date_joined",),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes":("wide",),
                "fields":("email","password1","password2","is_staff","is_active"),
            },
        ),
    )
    search_fields = ["email","username","last_name","first_name"]

admin.site.register(User,UserAdmin)

