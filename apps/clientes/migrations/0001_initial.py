# Generated by Django 2.0.2 on 2018-07-16 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core.Pessoa')),
                ('cliente_id', models.AutoField(auto_created=True, db_column='cliente_id', primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'CLIENTES',
                'ordering': ['pes_nome'],
            },
            bases=('core.pessoa',),
        ),
    ]
