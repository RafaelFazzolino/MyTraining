from pybrain.supervised import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork

from MyTraining.Training.dataset import create_dataset
from MyTraining.Training.models import ConfigNetwork
import numpy as np


def execute_rna(sexo, tipo_objetivo, tipo_preferencia, tipo_doenca, tipo_dias):

    #Create a dataset
    dataset = create_dataset()

    configs = ConfigNetwork.objects.all()

    config = configs[0]

    if config.bias is None:
        bias = False
    else:
        bias = True

    # dimensões de entrada e saida, argumento 2 é a quantidade de camadas intermediárias
    network = buildNetwork(dataset.indim, int(config.num_camadas), dataset.outdim, bias=bias)
    trainer = BackpropTrainer(network, dataset, learningrate=float(config.learningrate),
                              momentum=float(config.momentum))

    pesos_iniciais = network.params

    network._setParameters(np.random.uniform(config.peso_start, config.peso_end, network.params.shape[0]))

    error = 1.00000000

    epocasPercorridas = 0

    errors = []
    it = []
    while epocasPercorridas < config.epochs and error > config.erro_max:
        error = trainer.train()
        epocasPercorridas += 1
        errors.append(error)
        it.append(epocasPercorridas)
    graph = []
    idx = 0
    for e in errors:
        temp = []
        temp.append(idx)
        temp.append(e)
        idx += 1
        graph.append(temp)

    context = {
        'error': error,
        'epocas': epocasPercorridas,
        'pesos_iniciais': pesos_iniciais,
        'pesos_finais': network.params,
        'result': network.activate([sexo, tipo_objetivo, tipo_preferencia,
                                    tipo_doenca, tipo_dias]),
    }
    return context