from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpResponseRedirect, request, JsonResponse
from django.shortcuts import render, redirect

from .forms import ConvenioForm, EstagioForm, CursoForm, DisciplinaForm, PreceptorForm, LocalForm, EstabelecimentoForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import View
from .models import Convenio, Estagio, Curso, Disciplina, Preceptor, Local, Estabelecimento
from .render import Render


# Todas as classes que compõem o CRUD do sistema


class MyLoginView(SuccessMessageMixin, LoginView):
    success_url = reverse_lazy('dashboard')
    form_class = AuthenticationForm

    def form_invalid(self, form):
        messages.error(self.request, "Usuário e/ou senha inválidos, tente novamente!")
        return super().form_invalid(form)


class CursoCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'curso_form.html'
    success_url = reverse_lazy('cursolista')
    success_message = "Curso criado com sucesso!"


class CursoLista(LoginRequiredMixin, ListView):
    model = Curso
    template_name = 'curso_list.html'


class CursoRel(LoginRequiredMixin, ListView):
    model = Preceptor
    template_name = 'curso_rel.html'


class CursoUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'curso_form_update.html'
    success_url = reverse_lazy('cursolista')
    success_message = "Alterações feitas com sucesso!"


class CursoDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Curso
    form_class = CursoForm
    template_name = 'curso_confirm_delete.html'
    success_url = reverse_lazy('cursolista')
    success_message = "O curso foi deletado com sucesso!"

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.error(request, "Curso deletado com sucesso!")
        except ValueError:
            messages.error(request, 'Não foi possível deletar!')
            return redirect('cursodelete')

        return HttpResponseRedirect(success_url)


class CursoDetail(LoginRequiredMixin, DetailView):
    model = Curso
    template_name = 'curso_detail.html'


class ConvenioCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Convenio
    form_class = ConvenioForm
    template_name = 'convenio_form.html'
    success_url = reverse_lazy('conveniolista')
    success_message = "Convênio criado com sucesso!"


class ConvenioList(LoginRequiredMixin, ListView):
    model = Convenio
    template_name = 'convenio_list.html'

    def get_queryset(self):
        query = self.request.GET.get('convenio')
        if query:
            object_list = self.model.objects.filter(Q(razao_social__icontains=query)) | self.model.objects.filter(Q(
                email__icontains=query))
        else:
            object_list = self.model.objects.all()
        return object_list


class ConvenioRel(LoginRequiredMixin, ListView):
    model = Convenio
    template_name = 'convenio_rel.html'


class ConvenioDetail(DetailView):
    model = Convenio
    template_name = "convenio_detail.html"


class ConvenioUpdate(LoginRequiredMixin, UpdateView):
    model = Convenio
    form_class = ConvenioForm
    template_name = 'convenio_form_update.html'
    success_url = reverse_lazy('conveniolista')


class ConvenioDelete(LoginRequiredMixin, DeleteView):
    model = Convenio
    form_class = ConvenioForm
    template_name = 'convenio_delete_form.html'
    success_url = reverse_lazy('conveniolista')


class EstagioCreate(LoginRequiredMixin, CreateView):
    model = Estagio
    form_class = EstagioForm
    template_name = 'estagio_form.html'
    success_url = reverse_lazy('estagiolista')


class EstagioLista(LoginRequiredMixin, ListView):
    model = Estagio
    template_name = 'estagio_list.html'

    def get_queryset(self):
        query = self.request.GET.get('estagio')
        if query:
            object_list = self.model.objects.filter(setor__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list


class EstagioRel(LoginRequiredMixin, ListView):
    model = Estagio
    template_name = 'estagio_rel.html'


class EstagioDetail(LoginRequiredMixin, DetailView):
    model = Estagio
    template_name = 'estagio_detail.html'


class EstagioUpdate(LoginRequiredMixin, UpdateView):
    model = Estagio
    template_name = 'estagio_form_update.html'
    form_class = EstagioForm
    success_url = reverse_lazy('estagiolista')


class EstagioDelete(LoginRequiredMixin, DeleteView):
    model = Estagio
    form_class = EstagioForm
    template_name = 'estagio_confirm_delete.html'
    success_url = reverse_lazy('estagiolista')


class DisciplinaCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Disciplina
    form_class = DisciplinaForm
    template_name = 'disciplina_form.html'
    success_url = reverse_lazy('disciplinalista')
    success_message = "Disciplina criada com sucesso!"


class DisciplinaList(LoginRequiredMixin, ListView):
    model = Disciplina
    template_name = 'disciplina_list.html'

    def get_queryset(self):
        query = self.request.GET.get('disciplina')
        if query:
            object_list = self.model.objects.filter(nome__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list


class DisciplinaUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Disciplina
    form_class = DisciplinaForm
    template_name = 'disciplina_form_update.html'
    success_url = reverse_lazy('disciplinalista')
    success_message = "Disciplina atualizada com sucesso!"


class DisciplinaDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Disciplina
    form_class = DisciplinaForm
    template_name = 'disciplina_confirm_delete.html'
    success_url = reverse_lazy('disciplinalista')
    success_message = "Disciplina deletada com sucesso!"

    def form_valid(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DisciplinaDelete, self).delete(request, *args, **kwargs)


class DisciplinaDetail(LoginRequiredMixin, DetailView):
    model = Disciplina
    template_name = 'disciplina_detail.html'


class PreceptorCreate(LoginRequiredMixin, CreateView):
    model = Preceptor
    form_class = PreceptorForm
    template_name = 'preceptor_form.html'
    success_url = reverse_lazy('preceptorlista')


class PreceptorList(LoginRequiredMixin, ListView):
    model = Preceptor
    template_name = 'preceptor_list.html'

    def get_queryset(self):
        query = self.request.GET.get('preceptor')
        if query:
            object_list = self.model.objects.filter(matricula__icontains=query) | self.model.objects.filter(
                nome__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list


class PreceptorUpdate(LoginRequiredMixin, UpdateView):
    model = Preceptor
    template_name = 'preceptor_form_update.html'
    form_class = PreceptorForm
    success_url = reverse_lazy('preceptorlista')


class PreceptorDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Preceptor
    template_name = 'preceptor_confirm_delete.html'
    success_url = reverse_lazy('preceptorlista')
    success_message = "Preceptor deletado com sucesso!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class PreceptorDetail(LoginRequiredMixin, DetailView):
    model = Preceptor
    template_name = 'preceptor_detail.html'


def load_preceptores(request):
    disciplina_id = request.GET.get('disciplina')
    preceptores = Preceptor.objects.filter(disciplina_id=disciplina_id)
    return render(request, 'preceptores_dropdown_list.html', {'preceptores': preceptores})


def load_disciplinas(request):
    curso_id = request.GET.get('curso')
    disciplinas = Disciplina.objects.filter(curso_id=curso_id)
    return render(request, 'disciplinas_dropdown_list.html', {'disciplinas': disciplinas})


class LocalCreate(LoginRequiredMixin, CreateView):
    model = Local
    form_class = LocalForm
    template_name = 'local_form.html'
    success_url = reverse_lazy('listlocal')


class LocalList(LoginRequiredMixin, ListView):
    model = Local
    template_name = 'local_list.html'


class LocalUpdate(LoginRequiredMixin, UpdateView):
    model = Local
    template_name = 'local_form_update.html'
    form_class = LocalForm
    success_url = reverse_lazy('listlocal')


class LocalDelete(LoginRequiredMixin, DeleteView):
    model = Local
    form_class = LocalForm
    template_name = 'local_confirm_delete.html'
    success_url = reverse_lazy('listlocal')


class EstabelecimentoCreate(LoginRequiredMixin, CreateView):
    model = Estabelecimento
    form_class = EstabelecimentoForm
    template_name = 'estabelecimento_form.html'
    success_url = reverse_lazy('listestabelecimento')


class EstabelecimentoList(LoginRequiredMixin, ListView):
    model = Estabelecimento
    template_name = 'estabelecimento_list.html'


class EstabelecimentoUpdate(LoginRequiredMixin, UpdateView):
    model = Estabelecimento
    template_name = 'estabelecimento_form_update.html'
    form_class = EstabelecimentoForm
    success_url = reverse_lazy('listestabelecimento')


class EstabelecimentoDelete(LoginRequiredMixin, DeleteView):
    model = Estabelecimento
    form_class = EstabelecimentoForm
    template_name = 'estabelecimento_confirm_delete.html'
    success_url = reverse_lazy('listestabelecimento')


def custo_mensal():
    v = 0
    x = 0
    z = 0
    tat = 0
    for i in Estagio.objects.all():
        c = float(i.custo_por_aluno)
        v += c
        a = int(i.quantidade_de_alunos)
        z += a
        b = len(i.dates)
        x += b
        tat += float(v * x * z)
    return tat


def custo_anual():
    return custo_mensal() * 12


def custo_diario():
    for i in Estagio.objects.all():
        a = len(i.dates)
        return custo_mensal() / a
    return None


def aluno():
    total = 0
    for i in Estagio.objects.all():
        tot = i.quantidade_de_alunos
        total += tot
        if custo_mensal() != 0:
            return custo_mensal() / total
        return None
    return None


@login_required
def dash_board(request):
    estagios = Estagio.objects.all()
    return render(request, 'dashboard.html',
                  {'estagios': estagios, 'mensal': custo_mensal(), 'anual': custo_anual(), 'diario': custo_diario(),
                   'media': aluno()})


class PdfCurso(View, LoginRequiredMixin):

    def get_pdf(self, request):
        preceptor = Preceptor.objects.all()
        params = {
            'preceptor': preceptor,
            'request': request
        }
        return Render.render('relatoriocurso.html', params)


class PdfConvenio(View, LoginRequiredMixin):
    def get_pdf(self, request):
        convenio = Convenio.objects.all()
        params = {
            'convenio': convenio,
            'request': request
        }
        return Render.render('relatorioconvenio.html', params)


class PdfEstagio(View, LoginRequiredMixin):
    def get_pdf(self, request):
        estagio = Estagio.objects.all()
        params = {
            'estagio': estagio,
            'request': request
        }
        return Render.render('relatorioestagio.html', params)
