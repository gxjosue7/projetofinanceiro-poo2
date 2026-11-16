from abc import ABC, abstractmethod

from financeiro.lancamento import Lancamento


class Importador(ABC):

    @abstractmethod
    def importar(self, caminho):
        ...


class ImportadorBancoAlfa(Importador):

    def __init__(self, criador_leitor):
        self._criador_leitor = criador_leitor

    def importar(self, caminho):
        leitor = self._criador_leitor.criar(caminho)
        return leitor.ler(caminho)


class ImportadorBancoBeta(Importador):

    def __init__(self, criador_leitor):
        self._criador_leitor = criador_leitor

    def importar(self, caminho):
        leitor = self._criador_leitor.criar(caminho)
        lancamentos = leitor.ler(caminho)
        return [
            Lancamento(l.descricao, -l.valor, l.data, l.categoria)
            for l in lancamentos
        ]
