from abc import ABC, abstractmethod


class EstrategiaCorrecao(ABC):

    @abstractmethod
    def corrigir(self, valor, meses):
        ...


class CorrecaoIpca(EstrategiaCorrecao):

    def __init__(self, percentual_acumulado):
        if percentual_acumulado < 0:
            raise ValueError("Percentual nao pode ser negativo")
        self._percentual_acumulado = percentual_acumulado

    def corrigir(self, valor, meses):
        return valor * (1 + self._percentual_acumulado / 100)


class CorrecaoSelic(EstrategiaCorrecao):

    def __init__(self, taxa_mensal):
        if taxa_mensal < 0:
            raise ValueError("Taxa nao pode ser negativa")
        self._taxa_mensal = taxa_mensal

    def corrigir(self, valor, meses):
        return valor * (1 + self._taxa_mensal / 100) ** meses
