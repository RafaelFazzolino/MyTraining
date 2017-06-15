from django.shortcuts import render

from MyTraining.Training.forms import ConfigForm
from MyTraining.Training.models import ConfigNetwork


def inicio(request):
    context = {}
    return render(request, 'inicio.html', context)


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