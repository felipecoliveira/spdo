from django.shortcuts import render
from django.views.generic import ListView, View
from django.views.generic.edit import (CreateView, FormView,
                                       UpdateView, DeleteView)

from core.models import Area
from core.models import Uf
from core.models import TipoDocumento
from core.models import Pessoa
from core.models import Responsavel
from core.models import Protocolo

class HomeView(View):

    def get(self, request):
        return render(request, 'core/home.html')

class AreaView(ListView):
   model = Area
   context_object_name = 'areas'
   template_name = 'core/area/list.html'
   
class AreaCreate(CreateView):
   model = Area
   fields = ['sigla', 'nome']
   template_name = 'core/area/create.html'
   success_url = '/areas'

class AreaUpdate(UpdateView):
   model = Area
   success_url = '/areas'
   template_name = 'core/area/edit.html'

class UfView(ListView):
   model = Uf
   context_object_name = 'ufs'
   template_name = 'core/uf/list.html'
   
class UfCreate(CreateView):
   model = Uf
   fields = ['sigla', 'nome']
   template_name = 'core/uf/create.html'
   success_url = '/uf'

class UfUpdate(UpdateView):
   model = Uf
   success_url = '/uf'
   template_name = 'core/uf/edit.html'

class TipoDocumentoView(ListView):
   model = TipoDocumento
   context_object_name = 'tipodocumentos'
   template_name = 'core/tipodocumento/list.html'
   
class TipoDocumentoCreate(CreateView):
   model = TipoDocumento
   fields = ['nome']
   template_name = 'core/tipodocumento/create.html'
   success_url = '/tipodocumento'

class TipoDocumentoUpdate(UpdateView):
   model = TipoDocumento
   success_url = '/tipodocumento'
   template_name = 'core/tipodocumento/edit.html'

class PessoaView(ListView):
   model = Pessoa
   context_object_name = 'pessoas'
   template_name = 'core/pessoa/list.html'
   
class PessoaCreate(CreateView):
   model = Pessoa
   fields = ['nome', 'email', 'uf']
   template_name = 'core/pessoa/create.html'
   success_url = '/pessoa'

class PessoaUpdate(UpdateView):
   model = Pessoa
   success_url = '/pessoa'
   template_name = 'core/pessoa/edit.html' 

class ResponsavelView(ListView):
   model = Responsavel
   context_object_name = 'responsaveis'
   template_name = 'core/responsavel/list.html'
   
class ResponsavelCreate(CreateView):
   model = Responsavel
   fields = ['pessoa', 'data']
   template_name = 'core/responsavel/create.html'
   success_url = '/responsavel'

class ResponsavelUpdate(UpdateView):
   model = Responsavel
   success_url = '/responsavel'
   template_name = 'core/responsavel/edit.html'  

class ProtocoloView(ListView):
   model = Protocolo
   context_object_name = 'protocolos'
   template_name = 'core/protocolo/list.html'
   
class ProtocoloCreate(CreateView):
   model = Protocolo
   fields = ['seq', 'ano', 'dv', 'numero', 'data_protocolo', 'numero_documento', 'data_emissao'
            ,'assunto', 'usuario', 'tipo_documento', 'observacao']

   template_name = 'core/protocolo/create.html'
   success_url = '/protocolo'

class ProtocoloUpdate(UpdateView):
   model = Protocolo
   success_url = '/protocolo'
   template_name = 'core/protocolo/edit.html'     



