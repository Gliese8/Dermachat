# Generated by Django 5.0.6 on 2024-05-14 08:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("dermachat", "0002_alter_imagemetadata_malignant_and_more"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="imagemetadata",
            table="dermachat_database",
        ),
    ]
