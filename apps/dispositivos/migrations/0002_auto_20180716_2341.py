# Generated by Django 2.0.2 on 2018-07-16 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='url_img',
            field=models.ImageField(blank=True, db_column='url_img', null=True, upload_to='static/img/dispositivos/'),
        ),
    ]
