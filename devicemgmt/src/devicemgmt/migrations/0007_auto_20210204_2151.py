# Generated by Django 3.1.6 on 2021-02-04 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devicemgmt', '0006_auto_20210204_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
