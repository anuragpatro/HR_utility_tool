# Generated by Django 2.2.5 on 2019-12-18 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20191216_0100'),
        ('salary', '0005_auto_20191218_2211'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='monthly',
            new_name='monthly_salary',
        ),
    ]