# Generated by Django 4.2.11 on 2024-03-13 22:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("afbcore", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="address",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="address_verbatim",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
