# Generated by Django 2.1.3 on 2018-12-05 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='profile',
        ),
    ]
