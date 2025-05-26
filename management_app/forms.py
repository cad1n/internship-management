from django.forms import ModelForm
from .models import Convenio, Estagio, Curso, Disciplina, Preceptor, Local, Estabelecimento

tipoDeEstabelecimento = str('Tipo de Estabelecimento')


class ConvenioForm(ModelForm):
    class Meta:
        model = Convenio
        fields = ['concedente', 'endereco', 'unidade_executora', 'tipo_de_estabelecimento', 'representante',
                  'telefone', 'email', 'razao_social', 'cnpj', 'condicoes', 'descricao', 'data']


class EstagioForm(ModelForm):
    class Meta:
        model = Estagio
        fields = ['curso', 'disciplina', 'preceptor', 'quantidade_de_alunos',
                  'custo_por_aluno', 'turno', 'tipo_de_convenio', 'local',
                  'tipo_de_estabelecimento', 'setor', 'dates']


class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['nome_curso']


class DisciplinaForm(ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome_disciplina', 'curso']


class PreceptorForm(ModelForm):
    class Meta:
        model = Preceptor
        fields = ['nome_preceptor', 'matricula', 'disciplina', 'curso']


class LocalForm(ModelForm):
    class Meta:
        model = Local
        fields = ['nome_local']


class EstabelecimentoForm(ModelForm):
    class Meta:
        model = Estabelecimento
        fields = ['tipo']
