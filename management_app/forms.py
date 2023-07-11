from django.forms import ModelForm
from .models import Convenio, Estagio, Curso, Disciplina, Preceptor, Local, Estabelecimento
from bootstrap_datepicker_plus.widgets import DatePickerInput

tipoDeEstabelecimento = str('Tipo de Estabelecimento')


class ConvenioForm(ModelForm):
    class Meta:
        model = Convenio
        fields = ['concedente', 'endereco', 'unidade_executora', 'tipo_de_estabelecimento', 'representante',
                  'telefone', 'email', 'razao_social', 'cnpj', 'condicoes', 'descricao', 'data']
        widgets = {
            'data': DatePickerInput()
        }

    def __init__(self, *args, **kwargs):
        super(ConvenioForm, self).__init__(*args, **kwargs)
        self.fields['razao_social'].widget.attrs['placeholder'] = 'Razão Social'
        self.fields['unidade_executora'].widget.attrs['placeholder'] = 'Unidade Executora'
        self.fields['endereco'].widget.attrs['placeholder'] = 'Endereço'
        self.fields['tipo_de_estabelecimento'].widget.attrs['placeholder'] = tipoDeEstabelecimento
        self.fields['cnpj'].widget.attrs['placeholder'] = 'CNPJ'
        self.fields['representante'].widget.attrs['placeholder'] = 'Representante'
        self.fields['concedente'].widget.attrs['placeholder'] = 'Concedente'
        self.fields['telefone'].widget.attrs['placeholder'] = 'Telefone'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['descricao'].widget.attrs['placeholder'] = 'Descrição'
        self.fields['condicoes'].widget.attrs['placeholder'] = 'Condições'


class EstagioForm(ModelForm):
    class Meta:
        model = Estagio
        fields = ['curso', 'disciplina', 'preceptor', 'quantidade_de_alunos',
                  'custo_por_aluno', 'turno', 'tipo_de_convenio', 'local',
                  'tipo_de_estabelecimento', 'setor', 'dates']
        widgets = {
            'dates': DatePickerInput()
        }

    def __init__(self, *args, **kwargs):
        super(EstagioForm, self).__init__(*args, **kwargs)
        self.fields['quantidade_de_alunos'].widget.attrs['placeholder'] = 'Qtd de Alunos'
        self.fields['preceptor'].widget.attrs['placeholder'] = 'Preceptor'
        self.fields['custo_por_aluno'].widget.attrs['placeholder'] = 'Custo por Aluno'
        self.fields['tipo_de_convenio'].widget.attrs['placeholder'] = 'Convênio'
        self.fields['local'].widget.attrs['placeholder'] = 'Local'
        self.fields['tipo_de_estabelecimento'].widget.attrs['placeholder'] = tipoDeEstabelecimento
        self.fields['setor'].widget.attrs['placeholder'] = 'Setor'


class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['nome_curso']

    def __init__(self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)
        self.fields['nome_curso'].widget.attrs['placeholder'] = 'Nome do Curso'


class DisciplinaForm(ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome_disciplina']

    def __init__(self, *args, **kwargs):
        super(DisciplinaForm, self).__init__(*args, **kwargs)
        self.fields['nome_disciplina'].widget.attrs['placeholder'] = 'Nome'


class PreceptorForm(ModelForm):
    class Meta:
        model = Preceptor
        fields = ['nome_preceptor', 'matricula', 'curso', 'disciplina']

    def __init__(self, *args, **kwargs):
        super(PreceptorForm, self).__init__(*args, **kwargs)
        self.fields['nome_preceptor'].widget.attrs['placeholder'] = 'Nome'
        self.fields['matricula'].widget.attrs['placeholder'] = 'RGM'


class LocalForm(ModelForm):
    class Meta:
        model = Local
        fields = ['nome_local']

    def __init__(self, *args, **kwargs):
        super(LocalForm, self).__init__(*args, **kwargs)
        self.fields['nome_local'].widget.attrs['placeholder'] = 'Nome'


class EstabelecimentoForm(ModelForm):
    class Meta:
        model = Estabelecimento
        fields = ['tipo']

    def __init__(self, *args, **kwargs):
        super(EstabelecimentoForm, self).__init__(*args, **kwargs)
        self.fields['tipo'].widget.attrs['placeholder'] = tipoDeEstabelecimento
