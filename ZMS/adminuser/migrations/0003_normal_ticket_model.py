# Generated by Django 2.2.14 on 2020-09-24 09:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminuser', '0002_employeesmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Normal_ticket_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult', models.IntegerField()),
                ('children', models.IntegerField()),
                ('date', models.DateField(default=datetime.date(2020, 9, 24))),
                ('total', models.IntegerField()),
            ],
        ),
    ]
