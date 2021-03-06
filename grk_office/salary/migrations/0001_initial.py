# Generated by Django 2.2.5 on 2019-12-10 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basicpay', models.DecimalField(decimal_places=2, max_digits=9)),
                ('hra', models.DecimalField(decimal_places=2, max_digits=9)),
                ('transport', models.DecimalField(decimal_places=2, max_digits=9)),
                ('medical', models.DecimalField(decimal_places=2, max_digits=9)),
                ('prof_update', models.DecimalField(decimal_places=2, max_digits=9)),
                ('special_allowance', models.DecimalField(decimal_places=2, max_digits=9)),
                ('prof_tax', models.DecimalField(decimal_places=2, max_digits=9)),
                ('variable_pay', models.DecimalField(decimal_places=2, max_digits=9)),
                ('PF', models.DecimalField(decimal_places=2, max_digits=9)),
                ('ESI', models.DecimalField(decimal_places=2, max_digits=9)),
                ('total', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
    ]
