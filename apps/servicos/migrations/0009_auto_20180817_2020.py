# Generated by Django 2.0.2 on 2018-08-17 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0008_auto_20180721_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalordemservico',
            name='tipo_servico',
            field=models.CharField(choices=[('1', 'Troca de tela - completa'), ('2', 'Troca de touch'), ('3', 'Troca de LCD'), ('4', 'Troca auricular'), ('5', 'Troca microfone'), ('6', 'Troca bateria interna'), ('7', 'Troca carcaça - completa'), ('8', 'Troca carcaça - frontal'), ('9', 'Troca carcaça - traseira'), ('10', 'Troca componente - SMD'), ('11', 'Banho ultrasônico'), ('12', 'Troca auto-falante'), ('13', 'Software - atualização'), ('14', 'Software - reinstalação'), ('15', 'Software - conta google'), ('16', 'Software - genérico'), ('17', 'Base de Carga'), ('18', 'Análise'), ('19', 'Choque Bateria'), ('20', 'Orçamento')], db_column='tipo_servico', max_length=2),
        ),
        migrations.AlterField(
            model_name='ordemservico',
            name='tipo_servico',
            field=models.CharField(choices=[('1', 'Troca de tela - completa'), ('2', 'Troca de touch'), ('3', 'Troca de LCD'), ('4', 'Troca auricular'), ('5', 'Troca microfone'), ('6', 'Troca bateria interna'), ('7', 'Troca carcaça - completa'), ('8', 'Troca carcaça - frontal'), ('9', 'Troca carcaça - traseira'), ('10', 'Troca componente - SMD'), ('11', 'Banho ultrasônico'), ('12', 'Troca auto-falante'), ('13', 'Software - atualização'), ('14', 'Software - reinstalação'), ('15', 'Software - conta google'), ('16', 'Software - genérico'), ('17', 'Base de Carga'), ('18', 'Análise'), ('19', 'Choque Bateria'), ('20', 'Orçamento')], db_column='tipo_servico', max_length=2),
        ),
    ]