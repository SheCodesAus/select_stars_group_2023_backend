# Generated by Django 4.1.7 on 2023-03-23 02:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 22, 13, 39, 41, 621765)),
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('bio', models.TextField()),
                ('image', models.URLField(default='https://shecodes.com.au/wp-content/uploads/2021/10/Screen-Shot-2021-12-07-at-12.00.01-pm-400x400.png')),
                ('skills', models.CharField(max_length=500)),
                ('level', models.CharField(choices=[('Junior', 'Junior'), ('Industry', 'Industry'), ('Lead', 'Lead')], max_length=200, null=True)),
                ('interview', models.BooleanField(default=False)),
                ('offer', models.BooleanField(default=False)),
                ('contract_sent', models.BooleanField(default=False)),
                ('contract_return', models.BooleanField(default=False)),
                ('onboarding_completed', models.BooleanField(default=False)),
                ('feedback_sent', models.BooleanField(default=False)),
                ('offboarding', models.BooleanField(default=False)),
                ('events', models.ManyToManyField(blank=True, related_name='mentors', to='mentor.event')),
            ],
        ),
    ]
