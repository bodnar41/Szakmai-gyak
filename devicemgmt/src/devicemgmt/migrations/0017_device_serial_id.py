# Generated by Django 3.1.6 on 2021-02-09 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devicemgmt', '0016_auto_20210204_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='serial_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
