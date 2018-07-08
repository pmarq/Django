from django.contrib import admin
from .models import Carro, Montadora, Cliente, Fabricante, Peca, SuspensaoCarro,TerminalDirecao, Pivo, ArticulacaoAxial, AmortDt,AmortTras, kitAmortDt, kitAmortTras

admin.site.register(Cliente)
admin.site.register(Carro)
admin.site.register(Montadora)
admin.site.register(Fabricante)
admin.site.register(Peca)
admin.site.register(SuspensaoCarro)
admin.site.register(Pivo)
admin.site.register(TerminalDirecao)
admin.site.register(ArticulacaoAxial)
admin.site.register(AmortDt)
admin.site.register(AmortTras)
admin.site.register(kitAmortDt)
admin.site.register(kitAmortTras)



