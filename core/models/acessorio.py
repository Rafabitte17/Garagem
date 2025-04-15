from django.db import  models


class Acessesrio(models.Model):
    discricao = models.CharField(max_length=100)

    def __str__(self):
        return  f"({self.id} {self.descricao})"