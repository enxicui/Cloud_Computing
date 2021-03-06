# Generated by Django 2.2.4 on 2019-11-30 15:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eventsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='event_description',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='event_name',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='event_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(default='Dublin', max_length=200),
        ),
    ]
