# Generated by Django 2.2.5 on 2019-12-18 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0004_monthly'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthly',
            name='month',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='monthly',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
