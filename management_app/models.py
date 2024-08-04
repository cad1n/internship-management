from django.core.validators import MaxValueValidator, RegexValidator, MinValueValidator
from django.db import models
from django.db.models.functions import Upper
from management_app.utils import validate_cnpj
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _

lettervalidator = RegexValidator('^[0-9a-zàãáâéêíóôúA-Z ç]*$',
                                 'Apenas letras são permitidas e/ou números positivos são permitidos')

phonevalidator = RegexValidator(r"\([0-9]{2}\)[0-9]{4,5}-[0-9]{4}")

TURNO_CHOICES = [
    ('Manhã', 'Manhã'),
    ('Tarde', 'Tarde'),
    ('Noite', 'Noite'),
    ('Integral', 'Integral')
]

CONCEDENTE_CHOICES = [
    ('Estado', 'Estado'),
    ('Município', 'Município'),
    ('Instituição Filantrópica', 'Instituição Filantrópica')
]


class Setor(models.Model):
    id_setor = models.AutoField(primary_key=True)
    setor = models.CharField(max_length=30, null=False,
                             blank=False, default=None, validators=[lettervalidator])

    def __str__(self):
        return self.setor

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'
        constraints = [
            models.UniqueConstraint(Upper('setor'), name='unique_upper_sector_category')
        ]


class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nome_curso = models.CharField(max_length=30, null=False,
                                  blank=False, unique=True, default=None, validators=[lettervalidator])

    def __str__(self):
        return self.nome_curso

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        constraints = [
            models.UniqueConstraint(Upper('nome_curso'), name='unique_upper_nomecurso_category')
        ]


class Disciplina(models.Model):
    id_disciplina = models.AutoField(primary_key=True)
    nome_disciplina = models.CharField(max_length=40, null=False, blank=False, unique=True,
                                       validators=[lettervalidator])
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, default=None)

    def __str__(self):
        return self.nome_disciplina

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
        constraints = [
            models.UniqueConstraint(Upper('nome_disciplina'), name='unique_upper_nomedisciplina_category')
        ]


class Preceptor(models.Model):
    id_preceptor = models.AutoField(primary_key=True)
    nome_preceptor = models.CharField(max_length=40, null=False,
                                      blank=False, default=None, unique=True)
    matricula = models.PositiveIntegerField(
        unique=True, blank=False, null=False, default=None, verbose_name="RGM",
        validators=[MaxValueValidator(99999999)])
    disciplina = models.ForeignKey(
        Disciplina, null=False, on_delete=models.CASCADE, default=None)
    curso = models.ForeignKey(
        Curso, null=False, blank=False, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_preceptor

    class Meta:
        verbose_name = 'Preceptor'
        verbose_name_plural = 'Preceptores'
        constraints = [
            models.UniqueConstraint(Upper('nome_preceptor'), name='unique_upper_nomepreceptor_category')
        ]


class Local(models.Model):
    id_local = models.AutoField(primary_key=True)
    nome_local = models.CharField(max_length=30, null=False,
                                  blank=False, default=None, unique=True, validators=[lettervalidator])

    def __str__(self):
        return self.nome_local

    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locais'
        constraints = [
            models.UniqueConstraint(Upper('nome_local'), name='unique_upper_nomelocal_category'),
        ]


class Estabelecimento(models.Model):
    id_estabelecimento = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=30, null=False,
                            blank=False, default=None, unique=True, validators=[lettervalidator])

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = 'Estabelecimento'
        verbose_name_plural = 'Estabelecimentos'
        constraints = [
            models.UniqueConstraint(Upper('tipo'), name='unique_upper_tipo_category')
        ]


class Convenio(models.Model):
    id_convenio = models.AutoField(primary_key=True)
    concedente = models.CharField(
        choices=CONCEDENTE_CHOICES, null=False, blank=False, max_length=50)
    razao_social = models.CharField(max_length=50, null=False, blank=False, default=None,
                                    verbose_name="Razão Social", unique=True, validators=[lettervalidator])
    cnpj = models.CharField(unique=True, blank=False, max_length=14, validators=[
        validate_cnpj], verbose_name='CNPJ')
    unidade_executora = models.CharField(max_length=20, null=False, blank=False, default=None,
                                         verbose_name='Unidade Executora', validators=[lettervalidator])
    tipo_de_estabelecimento = models.ForeignKey(Estabelecimento, max_length=30, null=False, blank=False,
                                                default=None,
                                                verbose_name="Tipo de Estabelecimento", on_delete=models.CASCADE)
    representante = models.CharField(max_length=50, blank=False, default=None, validators=[lettervalidator])
    endereco = models.CharField(
        max_length=50, null=False, blank=False, default=None, verbose_name="Endereço")
    telefone = models.CharField(null=False, blank=False, max_length=14, validators=[phonevalidator])
    email = models.EmailField(
        max_length=30, null=False, blank=False, unique=True, default=None)
    descricao = models.TextField(
        max_length=1000, null=False, default=None, blank=False, verbose_name="Descrição")
    condicoes = models.TextField(
        max_length=1000, null=False, default=None, blank=False, verbose_name="Condições")
    data = ArrayField(models.DateField(max_length=256), size=256, verbose_name='Data')

    def __str__(self):
        return self.razao_social

    class Meta:
        verbose_name = 'Convênio'
        verbose_name_plural = 'Convênios'
        constraints = [
            models.UniqueConstraint(Upper('razao_social'), name='unique_upper_razaosocial_category'),
            models.UniqueConstraint(Upper('unidade_executora'), name='unique_upper_unidadeexecutora_category'),
            models.UniqueConstraint(Upper('endereco'), name='unique_upper_endereco_category'),
        ]


class Estagio(models.Model):
    id_estagio = models.AutoField(primary_key=True)
    curso = models.OneToOneField(
        'Curso',
        null=False,
        blank=False,
        unique=True,
        on_delete=models.CASCADE
    )
    disciplina = models.OneToOneField(
        'Disciplina',
        null=False,
        blank=False,
        unique=True,
        on_delete=models.CASCADE
    )
    preceptor = models.ForeignKey(
        'Preceptor',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    tipo_de_convenio = models.OneToOneField(
        'Convenio',
        null=False,
        blank=False,
        unique=True,
        on_delete=models.CASCADE,
        verbose_name=_("Concedente")
    )
    local = models.ForeignKey(
        'Local',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    tipo_de_estabelecimento = models.ForeignKey(
        'Estabelecimento',
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name=_("Tipo de Estabelecimento")
    )
    setor = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        validators=[lettervalidator]
    )
    quantidade_de_alunos = models.IntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1)],
        verbose_name=_("Qtd de Alunos")
    )
    turno = models.CharField(
        choices=TURNO_CHOICES,
        null=False,
        blank=False,
        max_length=50
    )
    custo_por_aluno = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        validators=[MinValueValidator(0.00)]
    )
    dates = ArrayField(
        models.DateField(),
        size=256,
        verbose_name=_('Data')
    )

    def __str__(self):
        return self.tipo_de_convenio.razao_social

    class Meta:
        verbose_name = _("Estágio")
        verbose_name_plural = _("Estágios")


class Relatorio(models.Model):
    id_relatorio = models.AutoField(primary_key=True)
    relatorio = models.CharField(
        max_length=80, null=False, blank=False, default=None)
