# Generated by Django 2.2.5 on 2019-12-10 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20191211_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='aadhar',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]