from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Classe controle token login rest-framework
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# Classe controle de data/hora de criacao e modificacao.
class TimeStamped(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Classe controle se foi visualizado ou nao.
class Displayable(models.Model):
    class Meta:
        abstract = True

    status = models.BooleanField(default=True)


#  ========================================= MODELO_PESSOA ===================================================
class Pessoa(TimeStamped, Displayable):
    pes_id = models.AutoField(db_column='pes_id', primary_key=True, unique=True, null=False, serialize=False)
    pes_nome = models.CharField(db_column='pes_nome', null=False, blank=False, max_length=80)
    pes_cpf = models.CharField(db_column='pes_cpf', null=True, blank=True, max_length=11)
    pes_rg = models.CharField(db_column='pes_rg', null=True, blank=True, max_length=20)
    pes_telefone = models.CharField(db_column='pes_telefone', null=True, blank=True, max_length=16)
    pes_celular = models.CharField(db_column='pes_celular', null=True, blank=True, max_length=17)
    pes_email = models.CharField(db_column='pes_email', null=True, blank=True, max_length=50)

    class Meta:
        ordering = ['-pes_id']
        db_table = 'PESSOAS'

    def __str__(self):
        return self.pes_nome



