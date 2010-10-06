from datetime import datetime
from django.db import models

class Artigo(models.Model):
    class Meta:
        ordering = ('-publicacao',)

    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    publicacao = models.DateTimeField(default=datetime.now, blank=True)

    def get_absolute_url(self):
        return '/artigo/%d/'%self.id

