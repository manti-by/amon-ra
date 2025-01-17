# Generated by Django 5.0.2 on 2024-03-04 11:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Sensor",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("external_id", models.IntegerField(unique=True)),
                ("sensor_id", models.CharField(max_length=32)),
                ("temp", models.DecimalField(decimal_places=2, max_digits=5)),
                ("humidity", models.DecimalField(decimal_places=2, max_digits=5)),
                ("created_at", models.DateTimeField(db_index=True)),
            ],
            options={
                "verbose_name": "sensor",
                "verbose_name_plural": "sensors",
            },
        ),
    ]
