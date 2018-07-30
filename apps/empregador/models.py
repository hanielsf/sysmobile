# Django
from django.db import models

# Local
from djmoney.models.fields import MoneyField
from apps.core.models import TimeStamped, Displayable
from .choices import *


#  ==================================== MODELO_LOTACAO ====================================================
class Lotacao(TimeStamped, Displayable):
    lot_codigo = models.CharField(db_column='lot_id', max_length=30, primary_key=True)
    lot_tipo = models.CharField(max_length=3, choices=TIPO_DE_LOTACAO, db_column='lot_tipo')
    lot_cod_fpas = models.CharField(max_length=3, db_column='lot_cod_fpas')
    lot_cod_terceiros = models.CharField(max_length=4, db_column='lot_cod_terceiros')

    class Meta:
        ordering = ['-lot_codigo']
        db_table = 'LOTACOES'

    def __str__(self):
        return self.lot_codigo


#  ===================================== MODELO_SINDICATO ==================================================
class Sindicato(TimeStamped, Displayable):
    sind_codigo = models.CharField(db_column='sind_codigo', primary_key=True, max_length=45)
    sind_nome = models.CharField(db_column='sind_nome', max_length=60)
    sind_cnpj = models.CharField(db_column='sind_cnpj', max_length=14)

    class Meta:
        ordering = ['-sind_nome']
        db_table = 'SINDICATOS'

    def __str__(self):
        return self.sind_nome


#  ====================================== MODELO_FUNCAO ====================================================
class Funcao(TimeStamped, Displayable):
    #  basico
    func_id = models.AutoField(db_column='func_id', primary_key=True, unique=True, null=False,
                               serialize=False)
    func_desc = models.CharField(db_column='func_desc', max_length=100)
    func_cbo = models.CharField(db_column='func_cbo', max_length=6)

    #  cargo publico
    func_acum_cargos = models.CharField(db_column='func_acum_cargos', choices=FUNC_ACUM_CARGOS,
                                        null=True, blank=True, max_length=1)
    func_cont_tempo_espc = models.CharField(db_column='func_cont_tempo_espc', choices=FUNC_CONT_TEMPO_ESPC,
                                            null=True, blank=True, max_length=1)
    func_cargo_exclusivo = models.CharField(db_column='func_cargo_exclusivo', choices=FUNC_CARGO_EXCLUSIVO,
                                            null=True, blank=True, max_length=1)
    func_lei_cargo = models.CharField(db_column='func_lei_cargo', max_length=60, null=True, blank=True)
    func_data_lei_cargo = models.DateField(db_column='func_data_lei_cargo', null=True, blank=True)
    func_situacao_lei_cargo = models.CharField(db_column='func_situacao_lei_cargo', choices=FUNC_SITUACAO_LEI_CARGO,
                                               null=True, blank=True, max_length=1)

    class Meta:
        ordering = ['-func_id']
        db_table = 'FUNCOES'

    def __str__(self):
        return self.func_desc


#  ===================================== MODELO_ESTABELECIMENTO =============================================
class Estabelecimento(TimeStamped, Displayable):
    est_id = models.AutoField(db_column='est_id', primary_key=True, unique=True, null=False, serialize=False)
    est_tipo_insc = models.CharField(db_column='est_tipo_insc', choices=TIPO_INSCRICAO, max_length=1)
    est_inscricao = models.CharField(db_column='est_inscricao', max_length=18)
    est_cnae_prep = models.CharField(db_column='est_cnae_prep', max_length=9)
    est_aliquota_rat = models.CharField(db_column='est_aliquota_rat', max_length=3)
    est_fap = models.CharField(db_column='est_fap', max_length=23, null=True, blank=True)

    #  endereco
    est_cep = models.CharField(db_column='est_cep', max_length=9, null=True, blank=True)
    est_logradouro = models.CharField(db_column='est_logradouro', max_length=80, null=True, blank=True)
    est_numero = models.CharField(db_column='est_numero', max_length=8, null=True, blank=True)
    est_bairro = models.CharField(db_column='est_bairro', max_length=30, null=True, blank=True)
    est_complemento = models.CharField(db_column='est_complemento', max_length=30, null=True, blank=True)
    est_cidade = models.CharField(db_column='est_cidade', max_length=30, null=True, blank=True)
    est_estado = models.CharField(db_column='est_estado', max_length=30, null=True, blank=True)

    #  comercial
    est_telefone = models.CharField(db_column='est_telefone', max_length=14, null=True, blank=True)
    est_denominacao = models.CharField(db_column='est_denominacao', max_length=80, null=True, blank=True)

    class Meta:
        ordering = ['-est_id']
        db_table = 'ESTABELECIMENTOS'

    def __str__(self):
        return self.est_denominacao


#  ===================================== MODELO_EMPREGADOR =====================================================
class Empregador(TimeStamped, Displayable):
    emp_cnjp = models.CharField(db_column='emp_cnpj', primary_key=True, max_length=14)
    emp_razao_social = models.CharField(db_column='emp_razao_social', max_length=115)
    emp_classificacao_tributaria = models.CharField(db_column='emp_classficacao_tributaria',
                                                    choices=CLASSIFICACAO_TRIBUTARIA, max_length=3)
    emp_natureza_jur = models.CharField(db_column='emp_natureza_jur', max_length=5)
    emp_contagem_dias_mens = models.CharField(db_column='emp_contagem_dias_mens', max_length=1)
    emp_cooperativa = models.CharField(db_column='emp_cooperativa', choices=COOPERATIVA, max_length=2)
    emp_construtora = models.BooleanField(db_column='emp_construtora', default=False)
    emp_desoneracao_folha = models.BooleanField(db_column='emp_desoneracao_folha', default=False)
    emp_regime_caixa = models.BooleanField(db_column='emp_regime_caixa', default=False)
    emp_reg_eletronico = models.BooleanField(db_column='emp_reg_eletronico', default=False)
    emp_fap = models.FloatField(db_column='emp_fap', max_length=14)
    emp_situacao_pj = models.CharField(db_column='emp_situacao_pj', choices=SITUACAO_PJ, max_length=2)

    #  contato
    emp_contato_nome = models.CharField(db_column='emp_contato_nome', max_length=60)
    emp_contato_cpf = models.CharField(db_column='emp_contato_cpf', max_length=14)
    emp_contato_fone = models.CharField(db_column='emp_contato_fone', max_length=14, null=True, blank=True)
    emp_contato_celular = models.CharField(db_column='emp_contato_celular', max_length=14, null=True, blank=True)

    class Meta:
        ordering = ['-emp_razao_social']
        db_table = 'EMPREGADORES'
        verbose_name = 'Empregador'
        verbose_name_plural = 'Empregadores'

    def __str__(self):
        return self.emp_razao_social


#  ===================================== MODELO_EMPREGADOR =====================================================
class Turno(TimeStamped, Displayable):
    tur_codigo = models.CharField(db_column='tur_codigo', primary_key=True, max_length=30)
    tur_hora_entrada = models.TimeField(db_column='tur_hora_entrada', auto_now=False, auto_now_add=False)
    tur_hora_saida = models.TimeField(db_column='tur_hora_saida', auto_now=False, auto_now_add=False)
    tur_intervalo_entrada = models.TimeField(db_column='tur_intervalo_entrada', auto_now=False, auto_now_add=False)
    tur_intervalo_saida = models.TimeField(db_column='tur_intervalo_saida', auto_now=False, auto_now_add=False)

    class Meta:
        ordering = ['-tur_codigo']
        db_table = 'TURNOS'

    def __str__(self):
        return self.tur_codigo


#  ===================================== MODELO_TOMADOR/SERVICO =====================================================
class TomadorServico(TimeStamped, Displayable):
    tom_inscricao = models.CharField(db_column='tom_inscricao', primary_key=True, max_length=18)
    tom_nome = models.CharField(db_column='tom_nome', max_length=45)
    tom_codigo_gps = models.CharField(db_column='tom_codigo_gps', max_length=4)
    colaboradores = models.ManyToManyField('colaboradores.Contratado')

    #  endereco
    tom_cep = models.CharField(db_column='tom_cep', max_length=9, null=True, blank=True)
    tom_logradouro = models.CharField(db_column='tom_logradouro', max_length=80)
    tom_numero = models.CharField(db_column='tom_numero', max_length=8, null=True, blank=True)
    tom_bairro = models.CharField(db_column='tom_bairro', max_length=30, null=True, blank=True)
    tom_complemento = models.CharField(db_column='tom_complemento', max_length=30, null=True, blank=True)
    tom_cidade = models.CharField(db_column='tom_cidade', max_length=30, null=True, blank=True)
    tom_estado = models.CharField(db_column='tom_estado', max_length=30, null=True, blank=True)

    class Meta:
        ordering = ['-tom_nome']
        db_table = 'TOMADORES_SERVICOS'

    def __str__(self):
        return self.tom_nome

