from django.contrib import admin

from helios.apps.sensors.models import Sensor


@admin.register(Sensor)
class SensorsAdmin(admin.ModelAdmin):
    list_display = ("name", "temp", "humidity", "created_at")
