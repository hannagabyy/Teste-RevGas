from django.db import models

# Create your models here.
class Banco(models.Model):

    codigo_de_compensacao = models.IntegerField(null=False,blank=False,unique=True)
    nome_da_instituicao = models.CharField(null=False,blank=False,max_length=200)

    class Meta:
        db_table='banco'

    def __str__(self):
        return self.nome_da_instituicao
    