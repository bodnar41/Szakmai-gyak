# Generated by Django 3.1.6 on 2021-02-04 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devicemgmt', '0015_auto_20210204_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='export_to_CSV',
        ),
        migrations.AlterField(
            model_name='device',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='devicemgmt.category'),
        ),
    ]
