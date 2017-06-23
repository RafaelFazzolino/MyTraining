from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class ConfigNetwork(models.Model):

    name = models.CharField(max_length=30, default="padrao")

    num_camadas = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(6)], default=4)
    bias = models.BooleanField(default=False)
    learningrate = models.FloatField(validators=[MinValueValidator(0),
                                       MaxValueValidator(1)], default=0.01)
    momentum = models.FloatField(validators=[MinValueValidator(0),
                                       MaxValueValidator(1)], default=0.99)
    epochs = models.IntegerField(default=1000)

    erro_max = models.FloatField(default=0.3)
    peso_start = models.FloatField(default=-1)
    peso_end = models.FloatField(default=1)

    def __str__(self):
        return self.name


class SugestResult(models.Model):
    tipo_sexo = models.IntegerField(default=1)
    tipo_objetivos = models.IntegerField(default=2)
    tipo_preferencias = models.IntegerField(default=1)
    tipo_doencas = models.IntegerField(default=1)
    tipo_dias = models.IntegerField(default=1)
    result1 = models.IntegerField(default=1)
    result2 = models.IntegerField(default=1)
    result3 = models.IntegerField(default=1)
    result = models.CharField(max_length=30)
