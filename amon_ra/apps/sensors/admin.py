from django.contrib import admin

from amon_ra.apps.sensors.models import Sensor


@admin.register(Sensor)
class SensorsAdmin(admin.ModelAdmin):
    list_display = ("sensor_id", "temp", "humidity", "created_at")
