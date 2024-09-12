# Generated by Django 5.1.1 on 2024-09-12 15:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shared", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="documentstate",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, db_index=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="documentstate",
            name="deleted_at",
            field=models.DateTimeField(
                blank=True, db_index=True, editable=False, null=True
            ),
        ),
        migrations.AddField(
            model_name="documentstate",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
