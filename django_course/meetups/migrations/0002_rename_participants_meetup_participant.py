# Generated by Django 3.2.7 on 2022-03-02 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meetup',
            old_name='participants',
            new_name='participant',
        ),
    ]
