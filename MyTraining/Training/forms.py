from django import forms


class ConfigForm(forms.Form):

    name = forms.CharField(max_length=30)
    num_camadas = forms.IntegerField()
    bias = forms.BooleanField(initial=False, required=False)
    learningrate = forms.FloatField()
    momentum = forms.FloatField()
    epochs = forms.IntegerField()
    erro_max = forms.FloatField()
    peso_start = forms.FloatField()
    peso_end = forms.FloatField()


class SugestForm(forms.Form):
    TREINO_CHOICES = (
        (1, "Alpha1"),
        (2, "Charlie"),
        (3, "Echo1"),
        (4, "Golf1"),
        (5, "Alpha + 1"),
        (6, "Charlie + 1"),
        (7, "Echo + 1"),
        (8, "Golf + 1"),
    )
    sugest = forms.ChoiceField(choices=TREINO_CHOICES)

class TreinadorForm(forms.Form):
    SEXO_CHOICES = (
        (1, "Masculino"),
        (2, "Feminino"),
    )

    OBJETIVOS = (
        (1, "Emagrecer"),
        (2, "Ganhar massa muscular"),
        (3, "Condicionamento Fisico"),
        (4, "Melhoria da Saúde"),
        (5, "Melhorar performance em outra atividade"),
        (6, "Definicao muscular"),
        (7, "Estetica"),
    )

    PREFERENCIAS = (
        (1, "bracos"),
        (2, "pernas"),
        (3, "peitoral"),
        (4, "costas"),
        (5, "gluteos"),
        (6, "abdominal"),
        (7, "Todos os grupos musculares"),
    )

    DOENCAS = (
        (1, "cardiovascular"),
        (2, "pulmonar"),
        (3, "diabetes"),
        (4, "degenerativa"),
        (5, "artrite"),
        (6, "artrose"),
        (7, "osteoporose"),
        (8, "lesao na coluna"),
        (9, "lesao articular"),
        (10, "lesao muscular"),
        (11, "cancer"),
        (12, "metabolica"),
        (13, "hepatica"),
        (14, "psiquiatrica/psicologica"),
        (15, "imunologica"),
        (16, "renal"),
        (17, "sindrome"),
        (18, "nenhuma"),
    )

    sexo = forms.ChoiceField(choices=SEXO_CHOICES)
    objetivos = forms.ChoiceField(choices=OBJETIVOS)
    preferencias = forms.ChoiceField(choices=PREFERENCIAS)
    doencas = forms.ChoiceField(choices=DOENCAS)
    dias = forms.IntegerField(max_value=7, min_value=1)



