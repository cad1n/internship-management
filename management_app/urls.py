# from django.urls import path
#
# from . import views
# from .views import ConvenioList, ConvenioCreate, ConvenioUpdate, ConvenioDelete, \
#     EstagioCreate, EstagioLista, EstagioDelete, EstagioUpdate, dash_board, \
#     ConvenioDetail, EstagioDetail, CursoLista, CursoCreate, CursoUpdate, CursoDelete, CursoDetail, \
#     DisciplinaCreate, DisciplinaList, DisciplinaUpdate, DisciplinaDelete, DisciplinaDetail, PreceptorCreate, \
#     PreceptorList, PreceptorUpdate, PreceptorDelete, PreceptorDetail, LocalCreate, LocalList, LocalUpdate, LocalDelete, \
#     EstabelecimentoCreate, EstabelecimentoList, EstabelecimentoUpdate, EstabelecimentoDelete, EstagioRel, CursoRel, \
#     ConvenioRel, PdfCurso, PdfConvenio, PdfEstagio
#
# urlpatterns = [
#
#     path('listaconvenio/', ConvenioList.as_view(), name="conveniolista"),
#     path('create', ConvenioCreate.as_view(), name="conveniocreate"),
#     path('update/<int:pk>/', ConvenioUpdate.as_view(), name="convenioupdate"),
#     path('delete/<int:pk>/', ConvenioDelete.as_view(), name="conveniodelete"),
#     path('detail/<int:pk>/', ConvenioDetail.as_view(), name="conveniodetail"),
#
#     path('listaestagio/', EstagioLista.as_view(), name="estagiolista"),
#     path('createestagio/', EstagioCreate.as_view(), name="estagiocreate"),
#     path('updateestagio/<int:pk>/', EstagioUpdate.as_view(), name="estagioupdate"),
#     path('deleteestagio/<int:pk>/', EstagioDelete.as_view(), name="estagiodelete"),
#     path('detailestagio/<int:pk>/', EstagioDetail.as_view(), name="estagiodetail"),
#
#     path('listacurso/', CursoLista.as_view(), name="cursolista"),
#     path('createcurso/', CursoCreate.as_view(), name="cursocreate"),
#     path('updatecurso/<int:pk>/', CursoUpdate.as_view(), name="cursoupdate"),
#     path('deletecurso/<int:pk>/', CursoDelete.as_view(), name="cursodelete"),
#     path('detailcurso/<int:pk>/', CursoDetail.as_view(), name="cursodetail"),
#
#     path('createdisciplina/', DisciplinaCreate.as_view(), name='createdisciplina'),
#     path('listadisciplina/', DisciplinaList.as_view(), name='disciplinalista'),
#     path('updatedisciplina/<int:pk>/', DisciplinaUpdate.as_view(), name='disciplinaupdate'),
#     path('deletedisciplina/<int:pk>/', DisciplinaDelete.as_view(), name='disciplinadelete'),
#     path('detaildisciplina/<int:pk>/', DisciplinaDetail.as_view(), name='disciplinadetail'),
#
#     path('createpreceptor/', PreceptorCreate.as_view(), name='createpreceptor'),
#     path('listapreceptor/', PreceptorList.as_view(), name='preceptorlista'),
#     path('updatepreceptor/<int:pk>/', PreceptorUpdate.as_view(), name='preceptorupdate'),
#     path('deletepreceptor/<int:pk>/', PreceptorDelete.as_view(), name='preceptordelete'),
#     path('detailpreceptor/<int:pk>/', PreceptorDetail.as_view(), name="preceptordetail"),
#
#     path('createlocal/', LocalCreate.as_view(), name='createlocal'),
#     path('listlocal/', LocalList.as_view(), name='listlocal'),
#     path('updatelocal/<int:pk>/', LocalUpdate.as_view(), name='updatelocal'),
#     path('deletelocal/<int:pk>/', LocalDelete.as_view(), name='deletelocal'),
#
#     path('createestabelecimento/', EstabelecimentoCreate.as_view(), name='createestabelecimento'),
#     path('listestabelecimento/', EstabelecimentoList.as_view(), name='listestabelecimento'),
#     path('updateestabelecimento/<int:pk>/', EstabelecimentoUpdate.as_view(), name='updateestabelecimento'),
#     path('deleteestabelecimento/<int:pk>/', EstabelecimentoDelete.as_view(), name='deleteestabelecimento'),
#
#     path('ajax/load-disciplinas/', views.load_disciplinas, name='ajax_load_disciplinas'),
#     path('ajax/load-preceptores/', views.load_preceptores, name='ajax_load_preceptores'),
#     path('pdfcurso/', PdfCurso.as_view(), name='pdfcurso'),
#     path('pdfconvenio/', PdfConvenio.as_view(), name='pdfconvenio'),
#     path('pdfestagio/', PdfEstagio.as_view(), name='pdfestagio'),
#     path('estagiorel', EstagioRel.as_view(), name='estagiorel'),
#     path('cursorel', CursoRel.as_view(), name='cursorel'),
#     path('conveniorel', ConvenioRel.as_view(), name='conveniorel'),
#
#     path('board/', dash_board, name="dashboard"),
# ]
