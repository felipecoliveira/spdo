from django.conf.urls import patterns, url
from core.views import (HomeView,AreaView, AreaCreate, AreaUpdate, 
						UfView, UfCreate, UfUpdate,
						TipoDocumentoView, TipoDocumentoCreate, TipoDocumentoUpdate,
                        PessoaView, PessoaCreate, PessoaUpdate,
                        ResponsavelView, ResponsavelCreate, ResponsavelUpdate,
                        ProtocoloView, ProtocoloCreate, ProtocoloUpdate)


urlpatterns = patterns(
    'core.views',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^areas$', AreaView.as_view(), name='areas'),
    url(r'^areas/cadastrar$', AreaCreate.as_view(), name='area_create'),
    url(r'^areas/editar/(?P<pk>\d+)$', AreaUpdate.as_view(), name='area_update'),
    url(r'^uf$', UfView.as_view(), name='ufs'),
    url(r'^uf/cadastrar$', UfCreate.as_view(), name='uf_create'),
    url(r'^uf/editar/(?P<pk>\d+)$', UfUpdate.as_view(), name='uf_update'),
    url(r'^tipodocumento$', TipoDocumentoView.as_view(), name='tipodocumentos'),
    url(r'^tipodocumento/cadastrar$', TipoDocumentoCreate.as_view(), name='tipodocumento_create'),
    url(r'^tipodocumento/editar/(?P<pk>\d+)$', TipoDocumentoUpdate.as_view(), name='tipodocumento_update'),
    url(r'^pessoa$', PessoaView.as_view(), name='pessoas'),
    url(r'^pessoa/cadastrar$', PessoaCreate.as_view(), name='pessoa_create'),
    url(r'^pessoa/editar/(?P<pk>\d+)$', PessoaUpdate.as_view(), name='pessoa_update'),
    url(r'^responsavel$', ResponsavelView.as_view(), name='responsaveis'),
    url(r'^responsavel/cadastrar$', ResponsavelCreate.as_view(), name='responsavel_create'),
    url(r'^responsavel/editar/(?P<pk>\d+)$', PessoaUpdate.as_view(), name='responsavel_update'),
    url(r'^protocolo$', ProtocoloView.as_view(), name='protocolos'),
    url(r'^protocolo/cadastrar$', ProtocoloCreate.as_view(), name='protocolo_create'),
    url(r'^protocolo/editar/(?P<pk>\d+)$', ProtocoloUpdate.as_view(), name='protocolo_update'),    
)

