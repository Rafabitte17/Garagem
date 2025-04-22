from django.db import models

from core.models.acessorio import Acessorio
from core.models.cor import Cor
from core.models.modelo import Modelo


class Veiculo(models.Model):
    nome = models.IntegerField(null=True , blank=True)
    preco = models.DecimalField(max_length=10 , decimal_places=2 , blank=True, default=0)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name='Veiculos', null=True, blank=True)
    cor = models.ForeignKey(Cor ,on_delete=models.PROTECT, related_name='Veiculos', null=True , blank=True )
    acessorio = models.ForeignKey(Acessorio, on_delete=models.PROTECT, related_name='Veiculos', null=True, blank=True)