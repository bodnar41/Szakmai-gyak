# Generated by Django 3.1.6 on 2021-02-04 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devicemgmt', '0011_auto_20210204_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devicemgmt.category'),
        ),
    ]