# Generated by Django 4.1.7 on 2023-03-22 00:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(default='https://shecodes.com.au/wp-content/uploads/2020/02/Purple_no_circle.svg')),
                ('event_type', models.CharField(choices=[('Flash', 'Flash'), ('Plus', 'Plus'), ('One Day Workshop', 'One Day Workshop')], max_length=200, null=True)),
                ('location', models.CharField(choices=[('Sydney', 'Sydney'), ('Perth', 'Perth'), ('Brisbane', 'Brisbane')], max_length=200, null=True)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField(default=datetime.datetime.now)),
                ('end_date', models.DateTimeField(default=datetime.datetime(2023, 4, 21, 11, 19, 57, 274665))),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
