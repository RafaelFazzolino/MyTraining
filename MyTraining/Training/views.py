from array import array

from django.shortcuts import render

from MyTraining.Training.forms import ConfigForm, TreinadorForm
from MyTraining.Training.models import ConfigNetwork
from MyTraining.Training.network import execute_rna


def inicio(request):
    context = {}
    if request.method == 'POST':
        form = TreinadorForm(request.POST)
        if form.is_valid():
            return render(request, 'result.html', generate_group(form.cleaned_data))
    else:
        form = TreinadorForm()
        context['form'] = form
        return render(request, 'inicio.html', context)


def generate_group(form):

    objetivos = form['objetivos']
    sexo = form['sexo']
    doencas = form['doencas']
    dias = form['dias']
    preferencias = form['preferencias']

    tipo_objetivo = 0
    tipo_preferencia = 0
    tipo_doenca = 0
    tipo_dias = 0

    if objetivos == 1 or objetivos == 4 or objetivos == 7 or objetivos == 3:
            tipo_objetivo = 1
    if objetivos == 2 or objetivos == 5 or objetivos == 6:
        tipo_objetivo = 2

    if preferencias == 1 or preferencias == 3 or preferencias == 4 or preferencias == 7:
        tipo_preferencia = 1
    if preferencias == 6 or preferencias == 2 or preferencias == 5:
        tipo_preferencia = 2

    if doencas == 1 or doencas == 2 or doencas == 5 or doencas == 6 or doencas == 7 or\
        doencas == 17 or doencas == 11 or doencas == 13 or doencas == 15 or doencas == 16:
        tipo_doenca = 1
    else:
        tipo_doenca = 2

    if 1 <= dias <= 3:
        tipo_dias = 1
    else:
        tipo_dias = 2

    result = execute_rna(sexo, tipo_objetivo, tipo_preferencia, tipo_doenca, tipo_dias)
    context = {
        'sexo': sexo,
        'objetivos': objetivos,
        'preferencias': preferencias,
        'doencas': doencas,
        'dias': dias,
        'result': result,
    }

    return context


def config(request):
    context = {}
    if request.method == 'POST':
        form = ConfigForm(request.POST)
        if form.is_valid():
            save_config(form.cleaned_data)
            return render(request, 'inicio.html', context)
    else:
        form = ConfigForm()
    context['form'] = form
    return render(request, 'config.html', context)


def integrantes(request):
    return render(request, 'integrantes.html')


def descricao(request):
    return render(request, 'descricao.html')


def ajuda(request):
    return render(request, 'ajuda.html')


def save_config(form):
    config = ConfigNetwork()
    config.name = form['name']
    config.num_camadas = form['num_camadas']
    config.bias = form['bias']
    config.peso_start = form['peso_start']
    config.peso_end = form['peso_end']
    config.epochs = form['epochs']
    config.erro_max = form['erro_max']
    config.momentum = form['momentum']
    config.learningrate = form['learningrate']
    config.save()