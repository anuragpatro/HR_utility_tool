# Generated by Django 2.2.5 on 2019-12-15 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20191211_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
