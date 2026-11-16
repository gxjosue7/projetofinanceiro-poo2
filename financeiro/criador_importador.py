from enum import Enum

from financeiro.importador import ImportadorBancoAlfa, ImportadorBancoBeta


class Banco(Enum):
    ALFA = "alfa"
    BETA = "beta"


class CriadorImportador:

    def __init__(self, criador_leitor):
        self._criador_leitor = criador_leitor

    def criar(self, banco):
        if banco == Banco.ALFA:
            return ImportadorBancoAlfa(self._criador_leitor)
        if banco == Banco.BETA:
            return ImportadorBancoBeta(self._criador_leitor)
        raise ValueError(f"Banco desconhecido: {banco}")
