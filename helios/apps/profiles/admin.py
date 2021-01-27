from django.contrib import admin

from helios.apps.profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ("user", "created_at")
    raw_id_fields = ("user",)
