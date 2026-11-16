class Aplicacao:

    def __init__(self, nome, valor, estrategia_rendimento):
        if valor <= 0:
            raise ValueError("Valor da aplicacao deve ser positivo")
        self.nome = nome
        self._valor = valor
        self._estrategia_rendimento = estrategia_rendimento

    @property
    def valor(self):
        return self._valor

    def calcular_rendimento(self):
        return self._estrategia_rendimento.calcular(self._valor)

    def calcular_valor_final(self):
        return self._valor + self.calcular_rendimento()
