class RegistroDiario:
    def __init__(self, data, sono_horas, estudo_horas, jogo_horas, celular_horas, esporte_horas, peso, gastos):
        self.data = data
        self.sono_horas = sono_horas
        self.estudo_horas = estudo_horas
        self.jogo_horas = jogo_horas
        self.celular_horas = celular_horas
        self.esporte_horas = esporte_horas
        self.peso = peso
        self.gastos = gastos

    def resumo(self):
        return f"{self.data} \nPeso:{self.peso} \nSono:{self.sono_horas} \nEstudo:{self.estudo_horas} \nGameplay:{self.jogo_horas} \nCelular:{self.celular_horas} \nEsportes:{self.esporte_horas} \nGastos:{self.gastos}"

    