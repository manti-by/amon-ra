# Generated by Django 5.0.3 on 2024-04-04 14:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptions", "0002_notification_client"),
    ]

    operations = [
        migrations.CreateModel(
            name="SubscriptionNotification",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Sent at")),
                (
                    "notification",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notification_logs",
                        to="subscriptions.notification",
                    ),
                ),
                (
                    "subscription",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notification_logs",
                        to="subscriptions.subscription",
                    ),
                ),
            ],
            options={
                "verbose_name": "subscription notification",
                "verbose_name_plural": "subscription notifications",
                "unique_together": {("subscription", "notification")},
            },
        ),
    ]