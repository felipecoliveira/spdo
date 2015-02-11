from django.contrib import admin

from core.models import Uf
from core.models import Pessoa
from core.models import Responsavel
from core.models import Area
from core.models import TipoDocumento
from core.models import Observacao
from core.models import Anexo
from core.models import Protocolo
from core.models import Situacao
from core.models import PessoaOrigem
from core.models import PessoaDestino
from core.models import TipoEntrega
from core.models import Notificacao
from core.models import Referencia
from core.models import TramiteInbox
from core.models import TramiteOutbox
from core.models import Fluxo
from core.models import Transicao
from core.models import Tramite

admin.site.register(Uf)
admin.site.register(Pessoa)
admin.site.register(Responsavel)
admin.site.register(Area)
admin.site.register(TipoDocumento)
admin.site.register(Observacao)
admin.site.register(Anexo)
admin.site.register(Protocolo)
admin.site.register(Situacao)
admin.site.register(PessoaOrigem)
admin.site.register(PessoaDestino)
admin.site.register(TipoEntrega)
admin.site.register(Notificacao)
admin.site.register(Referencia)
admin.site.register(TramiteInbox)
admin.site.register(TramiteOutbox)
admin.site.register(Fluxo)
admin.site.register(Transicao)
admin.site.register(Tramite)
