# Generated by Django 3.0.6 on 2020-10-16 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_match_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='adress',
            new_name='address',
        ),
    ]