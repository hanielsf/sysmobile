# Generated by Django 2.0.2 on 2018-07-25 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='pes_celular',
            field=models.CharField(blank=True, db_column='pes_celular', max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='pes_telefone',
            field=models.CharField(blank=True, db_column='pes_telefone', max_length=16, null=True),
        ),
    ]
