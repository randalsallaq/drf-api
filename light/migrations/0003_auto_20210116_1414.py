# Generated by Django 3.1.5 on 2021-01-16 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light', '0002_auto_20210116_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lightsample',
            name='price',
            field=models.TextField(max_length=600),
        ),
    ]
