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
   fields = ['sigla', 'nome']
   success_url = '/areas'
   template_name = 'core/area/edit.html'

class AreaDelete(DeleteView):
   model = Area
   context_object_name = 'area'
   template_name = 'core/area/confirm_delete.html'
   success_url = '/areas'

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
   fields = ['sigla', 'nome']
   success_url = '/uf'
   template_name = 'core/uf/edit.html'

class UfDelete(DeleteView):
   model = Uf
   context_object_name = 'uf'
   template_name = 'core/uf/confirm_delete.html'
   success_url = '/uf'   

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
   fields = ['nome']
   success_url = '/tipodocumento'
   template_name = 'core/tipodocumento/edit.html'

class TipoDocumentoDelete(DeleteView):
   model = TipoDocumento
   context_object_name = 'tipodocumento'
   template_name = 'core/tipodocumento/confirm_delete.html'
   success_url = '/tipodocumento'   

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
   fields = ['nome', 'email', 'uf']
   success_url = '/pessoa'
   template_name = 'core/pessoa/edit.html' 

class PessoaDelete(DeleteView):
   model = Pessoa
   context_object_name = 'pessoa'
   template_name = 'core/pessoa/confirm_delete.html'
   success_url = '/pessoa'   

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
   fields = ['pessoa', 'data']
   success_url = '/responsavel'
   template_name = 'core/responsavel/edit.html'

class ResponsavelDelete(DeleteView):
   model = Responsavel
   context_object_name = 'responsavel'
   template_name = 'core/responsavel/confirm_delete.html'
   success_url = '/responsavel'     

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
   fields = ['seq', 'ano', 'dv', 'numero', 'data_protocolo', 'numero_documento', 'data_emissao'
            ,'assunto', 'usuario', 'tipo_documento', 'observacao']
   success_url = '/protocolo'
   template_name = 'core/protocolo/edit.html'   

class ProtocoloDelete(DeleteView):
   model = Protocolo
   context_object_name = 'protocolo'
   template_name = 'core/protocolo/confirm_delete.html'
   success_url = '/protocolo'



