# Generated by Django 5.1.7 on 2025-03-13 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='entry',
            new_name='content',
        ),
    ]
