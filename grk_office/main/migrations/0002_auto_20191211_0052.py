# Generated by Django 2.2.5 on 2019-12-10 19:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='date',
            new_name='dateofbirth',
        ),
        migrations.AddField(
            model_name='person',
            name='dataofjoin',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='person',
            name='designation',
            field=models.CharField(max_length=30, null=True),
        ),
    ]