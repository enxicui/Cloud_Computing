# Generated by Django 2.2.4 on 2019-11-30 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventsapp', '0002_auto_20191130_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='event_date',
            field=models.CharField(max_length=200),
        ),
    ]