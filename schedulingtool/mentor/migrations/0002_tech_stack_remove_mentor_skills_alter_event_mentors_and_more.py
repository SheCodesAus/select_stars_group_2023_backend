# Generated by Django 4.1.7 on 2023-03-30 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tech_Stack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='skills',
        ),
        migrations.AlterField(
            model_name='event',
            name='mentors',
            field=models.ManyToManyField(related_name='events_mentor', to='mentor.mentor'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_tech_stack',
            field=models.ManyToManyField(related_name='events_tech', to='mentor.tech_stack'),
        ),
        migrations.AddField(
            model_name='mentor',
            name='mentor_tech_stack',
            field=models.ManyToManyField(related_name='tech_mentor', to='mentor.tech_stack'),
        ),
    ]