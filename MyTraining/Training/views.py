from array import array

from django.shortcuts import render

from MyTraining.Training.forms import ConfigForm, TreinadorForm, SugestForm
from MyTraining.Training.models import ConfigNetwork, SugestResult
from MyTraining.Training.network import execute_rna


def inicio(request):
    context = {}
    if request.method == 'POST':
        form = TreinadorForm(request.POST)
        if form.is_valid():
            return result(request, generate_group(form.cleaned_data))
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

    if objetivos == 1 or objetivos == 4 or objetivos == 7 or objetivos == 3:
        tipo_objetivo = 1
    else:
        tipo_objetivo = 2

    if preferencias == 1 or preferencias == 3 or preferencias == 4 or preferencias == 7:
        tipo_preferencia = 1
    else:
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
        'objetivos': tipo_objetivo,
        'preferencias': tipo_preferencia,
        'doencas': tipo_doenca,
        'dias': tipo_dias,
        'res': result['result'],
        'result': result['res'],
        'graph': result['graph'],
        'pesos_finais': result['pesos_finais'],
        'pesos_iniciais': result['pesos_iniciais'],
        'error': result['error'],
        'epocas': result['epocas'],
    }

    return context


def result(request, context):
    if request.method == 'POST':
        form = SugestForm(request.POST)
        if form.is_valid():
            save_sugest(form.cleaned_data)
            return render(request, 'inicio.html', context)
    else:
        form = SugestForm()
    context['form'] = form
    return render(request, 'result.html', context)


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


def save_sugest(form):
    sugest = SugestResult()
    sugest.tipo_sexo = form['sexo']
    sugest.tipo_objetivos = form['objetivos']
    sugest.tipo_preferencias = form['preferencias']
    sugest.tipo_doencas = form['doencas']
    sugest.tipo_dias = form['dias']
    sugest.result1 = form['result'][0]
    sugest.result2 = form['result'][1]
    sugest.result3 = form['result'][2]
    sugest.result = form['sugest']
    sugest.save()