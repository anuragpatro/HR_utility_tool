# Generated by Django 2.2.5 on 2019-12-10 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191211_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='dataofjoin',
            field=models.DateField(null=True),
        ),
    ]
