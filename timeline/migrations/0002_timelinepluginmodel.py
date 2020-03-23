# Generated by Django 2.2.11 on 2020-03-23 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('timeline', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimelinePluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='timeline_timelinepluginmodel', serialize=False, to='cms.CMSPlugin')),
                ('text', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]