from abc import ABC, abstractmethod


class LancamentoNaoEncontradoError(Exception):
    pass


class RepositorioLancamento(ABC):

    @abstractmethod
    def adicionar(self, lancamento):
        ...

    @abstractmethod
    def obter(self, id):
        ...

    @abstractmethod
    def listar(self):
        ...

    @abstractmethod
    def atualizar(self, lancamento):
        ...

    @abstractmethod
    def listar_por_categoria(self, nome):
        ...
