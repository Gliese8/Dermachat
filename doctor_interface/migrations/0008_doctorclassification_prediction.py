# Generated by Django 5.0.6 on 2024-05-21 15:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("doctor_interface", "0007_remove_doctorclassification_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctorclassification",
            name="prediction",
            field=models.FloatField(default=0.0),
        ),
    ]
