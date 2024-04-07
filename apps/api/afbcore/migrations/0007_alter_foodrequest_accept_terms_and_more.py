# Generated by Django 5.0.3 on 2024-04-06 22:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("afbcore", "0006_rename_highlighted_foodrequest_flagged"),
    ]

    operations = [
        migrations.AlterField(
            model_name="foodrequest",
            name="accept_terms",
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name="foodrequest",
            name="confirm_correct",
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name="foodrequest",
            name="flagged",
            field=models.BooleanField(default=False),
        ),
    ]