from meu_blog.tcc.models import Dados_Usuario
from meu_blog.tcc.models import Teste
from meu_blog.tcc.models import Bacteria
from meu_blog.tcc.models import Resultado
from meu_blog.tcc.models import Resultado_Final

django.contrib import admin

admin.site.register(Dados_Usuario)
admin.site.register(Teste)
admin.site.register(Bacteria)
admin.site.register(Resultado)
admin.site.register(Resultado_Final)

