from django.contrib import admin
from user.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class UserModelAdmin(UserAdmin):
    ordering = ('username',)
    list_display = ['first_name', 'username', 'id']
    list_display_links =['first_name', 'username', 'id']
    search_fields = ("username", "first_name")
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "phone")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password"),
            },
        ),
    )
    