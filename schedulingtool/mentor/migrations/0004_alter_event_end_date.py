# Generated by Django 4.1.7 on 2023-03-22 23:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0003_alter_event_end_date_mentor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 22, 10, 55, 55, 913305)),
        ),
    ]