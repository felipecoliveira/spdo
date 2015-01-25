from django.db import models

'''
  TODO: override de __str__ nos modelos
'''
class Uf(models.Model):
    sigla = models.CharField(max_length=2)
    nome = models.CharField(max_length=40)

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=30)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=50)
    uf = models.ForeignKey(Uf)
    telefone = models.CharField(max_length=30)
    cpf_cnpj = models.CharField(max_length=20)
    tipo_pessoa = models.CharField(max_length=1)
    contato = models.CharField(max_length=100)
    senha = models.CharField(max_length=20)

class Responsavel(models.Model):
    pessoa = models.ForeignKey(Pessoa)
    data = models.DateTimeField()

class Area(models.Model):
    sigla = models.CharField(max_length=20)
    nome = models.CharField(max_length=100)

class TipoDocumento(models.Model):
    nome = models.CharField(max_length=40)


class Observacao(models.Model):
    texto = models.CharField(max_length=2000) # qual o tam maximo?
    data_observacao = models.DateTimeField()
    usuario = models.CharField(max_length=50)

class Anexo(models.Model):
    arquivo = models.CharField(max_length=2000) # qual o tamanho maximo?
    tamanho = models.IntegerField()
    data_anexo = models.DateTimeField()
    usuario = models.CharField(max_length=50) # FK?

class Protocolo(models.Model):
   seq = models.IntegerField()
   ano = models.IntegerField()
   dv = models.IntegerField()
   numero = models.CharField(max_length=20)
   data_protocolo = models.DateTimeField()
   numero_documento = models.CharField(max_length=20)
   data_emissao = models.DateTimeField()
   assunto = models.CharField(max_length=100)
   usuario = models.CharField(max_length=50)
   tipo_documento = models.ForeignKey(TipoDocumento)
   observacao = models.ForeignKey(Observacao)
 
