from financeiro.repositorio_lancamento import (
    LancamentoNaoEncontradoError,
    RepositorioLancamento,
)


class RepositorioLancamentoMemoria(RepositorioLancamento):

    def __init__(self):
        self._lancamentos = {}
        self._proximo_id = 1

    def adicionar(self, lancamento):
        lancamento.atribuir_id(self._proximo_id)
        self._lancamentos[self._proximo_id] = lancamento
        self._proximo_id += 1

    def obter(self, id):
        if id not in self._lancamentos:
            raise LancamentoNaoEncontradoError(f"Lancamento {id} nao encontrado")
        return self._lancamentos[id]

    def listar(self):
        return list(self._lancamentos.values())

    def atualizar(self, lancamento):
        if lancamento.id is None or lancamento.id not in self._lancamentos:
            raise LancamentoNaoEncontradoError("Lancamento nunca foi adicionado")
        self._lancamentos[lancamento.id] = lancamento

    def listar_por_categoria(self, nome):
        return [l for l in self._lancamentos.values() if l.categoria.nome == nome]
