# Generated by Django 5.0.3 on 2024-03-21 09:50

import amon_ra.apps.core.services
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("key", models.UUIDField(default=amon_ra.apps.core.services.generate_uuid)),
                ("hash", models.UUIDField(default=amon_ra.apps.core.services.generate_uuid)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "client",
                "verbose_name_plural": "clients",
            },
        ),
    ]
