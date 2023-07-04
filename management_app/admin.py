from django.contrib import admin
from .models import Convenio, Curso, Estagio,\
     Local, Estabelecimento, Setor, Disciplina

admin.site.register(Convenio)
admin.site.register(Curso)
admin.site.register(Estagio)
admin.site.register(Local)
admin.site.register(Estabelecimento)
admin.site.register(Setor)
admin.site.register(Disciplina)
