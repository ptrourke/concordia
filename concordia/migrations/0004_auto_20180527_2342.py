# Generated by Django 2.0.5 on 2018-05-27 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concordia', '0003_asset_media_url_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='media_url_test',
            new_name='media_url_text',
        ),
    ]
