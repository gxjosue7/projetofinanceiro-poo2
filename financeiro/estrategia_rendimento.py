from abc import ABC, abstractmethod


class EstrategiaRendimento(ABC):

    @abstractmethod
    def calcular(self, valor_aplicado):
        ...


class RendimentoPoupanca(EstrategiaRendimento):

    PERCENTUAL_MENSAL = 0.5

    def calcular(self, valor_aplicado):
        return valor_aplicado * self.PERCENTUAL_MENSAL / 100


class RendimentoCdbPrefixado(EstrategiaRendimento):

    def __init__(self, percentual_mensal):
        if percentual_mensal < 0:
            raise ValueError("Percentual nao pode ser negativo")
        self._percentual_mensal = percentual_mensal

    def calcular(self, valor_aplicado):
        return valor_aplicado * self._percentual_mensal / 100
