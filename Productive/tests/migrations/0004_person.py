# Generated by Django 5.1.6 on 2025-03-28 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_rename_tests_testmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
            ],
        ),
    ]
