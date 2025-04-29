from django.db import models

class Veiculo(models.Model):
    ano = models.IntegerField(max_length=80) 
    marca = models.CharField(max_length=80)
    categoria = models.CharField(max_length=80)
    cor = models.ForeignKey('Cor', on_delete=models.PROTECT)
    acessorio = models.ForeignKey('Acessorio', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.ano} - {self.marca} - {self.categoria} - {self.cor} - {self.acessorio}'
