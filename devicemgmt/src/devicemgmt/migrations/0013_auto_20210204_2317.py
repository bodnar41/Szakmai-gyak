# Generated by Django 3.1.6 on 2021-02-04 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devicemgmt', '0012_auto_20210204_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
