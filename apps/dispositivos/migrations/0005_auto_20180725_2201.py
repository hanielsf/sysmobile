# Generated by Django 2.0.2 on 2018-07-25 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivos', '0004_auto_20180725_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='imei',
            field=models.CharField(blank=True, db_column='imei', max_length=15, null=True),
        ),
    ]
