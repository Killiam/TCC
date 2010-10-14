from django.db import models

# Create your models here.

class Dados_Usuario(models.Model):
    nome_teste =  models.CharField(max_length=30)
    chave_teste = models.CharField(max_length=5)

class Teste(models.Model):
    nome =  models.CharField(max_length=30)
    chave = models.CharField(max_length=5)

class Bacteria(models.Model):
    nome_bacteria =  models.CharField(max_length=50)
    nome_teste =     models.CharField(max_length=30)    
    chave_bacteria = models.CharField(max_length=5)

class Resultado(models.Model):
    nome_bacteria =  models.CharField(max_length=50)

class Resultado_Final(models.Model):
    nome_bacteria =  models.CharField(max_length=50)


