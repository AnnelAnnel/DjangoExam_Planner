# Generated by Django 3.0.8 on 2020-07-27 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0004_remove_meeting_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='duration',
            field=models.IntegerField(default=10),
        ),
    ]
