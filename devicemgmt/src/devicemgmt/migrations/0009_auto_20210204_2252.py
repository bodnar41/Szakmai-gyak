# Generated by Django 3.1.6 on 2021-02-04 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devicemgmt', '0008_auto_20210204_2246'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AlterField(
            model_name='device',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]