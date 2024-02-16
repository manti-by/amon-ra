from django.contrib import admin

from amon_ra.apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "is_staff", "is_superuser", "created_at", "updated_at")
    list_filter = ("is_staff", "is_superuser", "created_at")
    readonly_fields = ("password",)
    search_fields = ("email",)
    ordering = ("-updated_at",)
