# Generated by Django 3.2.3 on 2021-08-07 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edify', '0008_mathamatics_link1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='desc',
            new_name='suggestions',
        ),
    ]
