# Generated by Django 2.2.9 on 2020-01-24 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pootle_statistics', '0004_fill_translated_wordcount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submission',
            options={'base_manager_name': 'objects', 'get_latest_by': 'creation_time', 'ordering': ['creation_time', 'pk']},
        ),
    ]