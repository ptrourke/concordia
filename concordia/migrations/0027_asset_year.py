# Generated by Django 2.2b1 on 2019-02-22 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("concordia", "0026_merge_20190221_2128")]

    operations = [
        migrations.AddField(
            model_name="asset",
            name="year",
            field=models.CharField(blank=True, max_length=4),
        )
    ]
