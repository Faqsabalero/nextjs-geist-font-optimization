# Generated by Django 5.2.2 on 2025-06-05 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0012_rename_domicilio_customuser_ciudad_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="venta",
            name="session_key",
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
