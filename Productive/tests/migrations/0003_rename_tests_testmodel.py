# Generated by Django 5.1.6 on 2025-02-20 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_tests_join_date_tests_phone'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tests',
            new_name='TestModel',
        ),
    ]
