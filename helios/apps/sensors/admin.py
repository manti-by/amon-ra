from django.contrib import admin

from helios.apps.sensors.models import Sensor


@admin.register(Sensor)
class SensorsAdmin(admin.ModelAdmin):
    list_display = ("sensor_id", "temp", "humidity", "created_at")
