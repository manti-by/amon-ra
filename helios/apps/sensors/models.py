from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=255)
    temp = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"Sensor {self.name}"
