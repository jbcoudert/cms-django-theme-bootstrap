# Generated by Django 2.2.11 on 2020-03-23 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0002_timelinepluginmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timelinepluginmodel',
            name='text',
        ),
        migrations.AddField(
            model_name='timelinepluginmodel',
            name='events',
            field=models.ManyToManyField(to='timeline.Event'),
        ),
    ]
