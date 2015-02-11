from django.db import models

'''
  TODO: Adicionar campo Situacao na tabela Protocolo
'''
class Area(models.Model):
    sigla = models.CharField(max_length=20)
    nome = models.CharField(max_length=100)

    def __str__(self):
      return self.sigla

class Uf(models.Model):
    sigla = models.CharField(max_length=2)
    nome = models.CharField(max_length=40)

    def __str__(self):
      return self.sigla

class TipoDocumento(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
      return self.nome

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

    def __str__(self):
      return self.nome

class Responsavel(models.Model):
    pessoa = models.ForeignKey(Pessoa)
    data = models.DateTimeField()

    def __str__(self):
      return self.pessoa.nome

class Observacao(models.Model):
    texto = models.CharField(max_length=2000) # qual o tam maximo?
    data_observacao = models.DateTimeField()
    usuario = models.CharField(max_length=50)

    def __str__(self):
      return self.texto

class Anexo(models.Model):
    arquivo = models.CharField(max_length=2000) # qual o tamanho maximo?
    tamanho = models.IntegerField()
    data_anexo = models.DateTimeField()
    usuario = models.CharField(max_length=50) # FK?

    def __str__(self):
      return self.arquivo

class Situacao(models.Model):
   nome = models.CharField(max_length=40)
   inicial = models.IntegerField()
   final = models.IntegerField()

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
   situacao = models.ForeignKey(Situacao)

   def __str__(self):
      return self.seq

class PessoaOrigem(models.Model):
   protocolo = models.ForeignKey(Protocolo)
   pessoa = models.ForeignKey(Pessoa)

class TipoEntrega(models.Model):
   nome = models.CharField(max_length=40)

class PessoaDestino(models.Model):
   protocolo = models.ForeignKey(Protocolo)
   pessoa = models.ForeignKey(Pessoa)
   tipo_entrega = models.ForeignKey(TipoEntrega)

class Notificacao(models.Model):
   pessoa = models.ForeignKey(Pessoa)
   protocolo = models.ForeignKey(Protocolo)

class Referencia(models.Model):
   protocolo = models.ForeignKey(Protocolo, null=False, related_name='protocolo')
   referencia = models.ForeignKey(Protocolo, null=False, related_name='referencia')

class TramiteInbox(models.Model):
   protocolo = models.ForeignKey(Protocolo)
   area = models.ForeignKey(Area)

class TramiteOutbox(models.Model):
   protocolo = models.ForeignKey(Protocolo)
   area = models.ForeignKey(Area)

class Fluxo(models.Model):
   nome = models.CharField(max_length=40)
   tipo_documento = models.ForeignKey(TipoDocumento)
   
class Transicao(models.Model):
   fluxo = models.ForeignKey(Fluxo)
   area_origem = models.ForeignKey(Area, null=False, related_name='area_origem')
   area_destino = models.ForeignKey(Area, null=False, related_name='area_destino')

class Tramite(models.Model):
   protocolo = models.ForeignKey(Protocolo)
   area = models.ForeignKey(Area, null=False, related_name='area')
   data_disponibilidade = models.DateTimeField()
   data_recebimento = models.DateTimeField()
   acao = models.CharField(max_length=2000)
   copia = models.IntegerField()
   area_anterior = models.ForeignKey(Area, null=True, related_name='area_anterior')
   responsavel = models.ForeignKey(Responsavel)
   usuario = models.CharField(max_length=40)
