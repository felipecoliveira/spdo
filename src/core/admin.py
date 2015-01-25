from django.contrib import admin

from core.models import Uf
from core.models import Pessoa
from core.models import Responsavel
from core.models import Area
from core.models import TipoDocumento
from core.models import Observacao
from core.models import Anexo
from core.models import Protocolo

admin.site.register(Uf)
admin.site.register(Pessoa)
admin.site.register(Responsavel)
admin.site.register(Area)
admin.site.register(TipoDocumento)
admin.site.register(Observacao)
admin.site.register(Anexo)
admin.site.register(Protocolo)

