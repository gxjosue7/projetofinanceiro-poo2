from abc import ABC, abstractmethod


class EstrategiaJuros(ABC):

    @abstractmethod
    def calcular(self, capital, taxa_mensal, meses):
        ...


class JurosSimples(EstrategiaJuros):

    def calcular(self, capital, taxa_mensal, meses):
        if meses < 0:
            raise ValueError("Meses nao pode ser negativo")
        return capital * taxa_mensal / 100 * meses


class JurosCompostos(EstrategiaJuros):

    def calcular(self, capital, taxa_mensal, meses):
        if meses < 0:
            raise ValueError("Meses nao pode ser negativo")
        return capital * ((1 + taxa_mensal / 100) ** meses - 1)
