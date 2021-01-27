from django.contrib import admin

from helios.apps.sensors.models import Sensor, Photo


class CreatedByAdminMixin:
    def save_formset(self, request, form, formset, change):
        for f in formset.forms:
            obj = f.instance
            if isinstance(obj, Sensor):
                obj.created_by = request.user
            obj.save()
        formset.save()


@admin.register(Sensor)
class SensorsAdmin(CreatedByAdminMixin, admin.ModelAdmin):

    list_display = (
        "temp",
        "humidity",
        "moisture",
        "luminosity",
        "created_at",
        "updated_at",
    )
    raw_id_fields = ("created_by",)


@admin.register(Photo)
class PhotoAdmin(CreatedByAdminMixin, admin.ModelAdmin):

    list_display = ("file", "created_at", "updated_at")
    raw_id_fields = ("created_by",)
