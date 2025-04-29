from django.db import models
from core.models import Cor, Acessorio, Modelo

class Veiculo(models.Model):
    ano = models.IntegerField() 
    marca = models.CharField(max_length=80)
    categoria = models.CharField(max_length=80)
    cor = models.ForeignKey('Cor', on_delete=models.PROTECT)
    acessorio = models.ForeignKey('Acessorio', on_delete=models.PROTECT)
    modelo = models.ForeignKey('Modelo', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.ano} - {self.marca} - {self.categoria} - {self.cor} - {self.modelo.nome}'
