from django.forms import ModelForm

from bolsa.models import *


class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa

        fields = {'nome'}


class AcaoForm(ModelForm):
    class Meta:
        model = Acao

        fields = {'sigla', 'empresa'}

class CotacaoForm(ModelForm):
    class Meta:
        model = Cotacao

        fields = {'acao', 'valor', 'data'}