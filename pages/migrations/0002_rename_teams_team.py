# Generated by Django 4.1.1 on 2022-09-24 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Teams',
            new_name='Team',
        ),
    ]