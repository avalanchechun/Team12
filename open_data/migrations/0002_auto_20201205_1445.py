# Generated by Django 2.2.6 on 2020-12-05 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('open_data', '0001_initial'),
    ]

    operations = [


        migrations.RenameField(
            model_name='restaurant',
            old_name='city_id',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='country_id',
            new_name='country',
        ),
    ]
