from pybrain.datasets import SupervisedDataSet


def create_dataset():
    dataset = SupervisedDataSet(5, 3)

    # 1, 1, 1, 1, 2

    # Homens
    dataset.addSample([1, 1, 1, 1, 1], [1,1,1])  # Treino Alpha 1
    dataset.addSample([1, 1, 1, 1, 2], [1,1,1])  # Treino Alpha 2
    dataset.addSample([1, 1, 1, 2, 1], [1,1,1])  # Treino Bravo 1
    dataset.addSample([1, 1, 1, 2, 2], [1,1,1])  # Treino Bravo 2

    dataset.addSample([1, 1, 2, 1, 1], [1,1,2])  # Treino Charlie 1
    dataset.addSample([1, 1, 2, 1, 2], [1,1,2])  # Treino Charlie 2
    dataset.addSample([1, 1, 2, 2, 1], [1,1,2])  # Treino Delta 1
    dataset.addSample([1, 1, 2, 2, 2], [1,1,2])  # Treino Delta 2

    dataset.addSample([1, 2, 1, 1, 1], [1,2,1])  # Treino Echo 1
    dataset.addSample([1, 2, 1, 1, 2], [1,2,1])  # Treino Echo 2
    dataset.addSample([1, 2, 1, 2, 1], [1,2,1])  # Treino Fox 1
    dataset.addSample([1, 2, 1, 2, 2], [1,2,1])  # Treino Fox 2

    dataset.addSample([1, 2, 2, 1, 1], [1,2,2])  # Treino Golf 1
    dataset.addSample([1, 2, 2, 1, 2], [1,2,2])  # Treino Golf 2
    dataset.addSample([1, 2, 2, 2, 1], [1,2,2])  # Treino Hot 1
    dataset.addSample([1, 2, 2, 2, 2], [1,2,2])  # Treino Hot 2

    # Mulheres
    dataset.addSample([2, 1, 1, 1, 1], [2,1,1])  # Treino Alpha + 1
    dataset.addSample([2, 1, 1, 1, 2], [2,1,1])  # Treino Alpha + 2
    dataset.addSample([2, 1, 1, 2, 1], [2,1,1])  # Treino Bravo + 1
    dataset.addSample([2, 1, 1, 2, 2], [2,1,1])  # Treino Bravo + 2

    dataset.addSample([2, 1, 2, 1, 1], [2,1,2])  # Treino Charlie + 1
    dataset.addSample([2, 1, 2, 1, 2], [2,1,2])  # Treino Charlie + 2
    dataset.addSample([2, 1, 2, 2, 1], [2,1,2])  # Treino Delta + 1
    dataset.addSample([2, 1, 2, 2, 2], [2,1,2])  # Treino Delta + 2

    dataset.addSample([2, 2, 1, 1, 1], [2,2,1])  # Treino Echo + 1
    dataset.addSample([2, 2, 1, 1, 2], [2,2,1])  # Treino Echo + 2
    dataset.addSample([2, 2, 1, 2, 1], [2,2,1])  # Treino Fox + 1
    dataset.addSample([2, 2, 1, 2, 2], [2,2,1])  # Treino Fox + 2

    dataset.addSample([2, 2, 2, 1, 1], [2,2,2])  # Treino Golf + 1
    dataset.addSample([2, 2, 2, 1, 2], [2,2,2])  # Treino Golf + 2
    dataset.addSample([2, 2, 2, 2, 1], [2,2,2])  # Treino Hot + 1
    dataset.addSample([2, 2, 2, 2, 2], [2,2,2])  # Treino Hot + 2

    return dataset