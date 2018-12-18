from datetime import date

from django.shortcuts import render, redirect
from bolsa.forms import *

# Create your views here.
from bolsa.models import *



def inicio(request):

    return render(request, 'index.html')

def lista_empresas(request):

    return render(request, 'empresas.html', {'empresas': Empresa.objects.all()})

def lista_acoes(request):

    return render(request, 'acoes.html', {'acoes': Acao.objects.all()})

def lista_cotacoes(request):

    return render(request, 'cotacoes.html', {'cotacoes': Cotacao.objects.all()})

def add_empresa(request):
    if request.method == "POST":
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empresas')
    else:
        form = EmpresaForm()
        return render(request, "add_empresa.html", {'form': form})

def add_acao(request):
    if request.method == "POST":
        form = AcaoForm(request.POST)
        if form.is_valid():
            acao = form.save(commit=False)
            acao.data_inicio = date.today()
            acao.save()
            return redirect('acoes')
    else:
        form = AcaoForm()
        return render(request, 'add_acao.html', {'form': form})

def add_cotacao(request):
    if request.method == "POST":
        form = CotacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cotacoes')
    else:
        form = CotacaoForm()
        return render(request, 'add_cotacao.html', {'form': form})