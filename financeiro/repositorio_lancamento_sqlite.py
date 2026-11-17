from financeiro.categoria import Categoria
from financeiro.lancamento import Lancamento
from financeiro.repositorio_lancamento import (
    LancamentoNaoEncontradoError,
    RepositorioLancamento,
)

COLUNAS = "id, descricao, valor, data, categoria"


class RepositorioLancamentoSQLite(RepositorioLancamento):

    def __init__(self, conexao):
        self._conexao = conexao

    def adicionar(self, lancamento):
        with self._conexao:
            cursor = self._conexao.execute(
                "INSERT INTO lancamento (descricao, valor, data, categoria) "
                "VALUES (?, ?, ?, ?)",
                (
                    lancamento.descricao,
                    lancamento.valor,
                    lancamento.data,
                    lancamento.categoria.nome,
                ),
            )
        lancamento.atribuir_id(cursor.lastrowid)

    def obter(self, id):
        linha = self._conexao.execute(
            f"SELECT {COLUNAS} FROM lancamento WHERE id = ?", (id,)
        ).fetchone()
        if linha is None:
            raise LancamentoNaoEncontradoError(f"Lancamento {id} nao encontrado")
        return self._reconstituir(linha)

    def listar(self):
        linhas = self._conexao.execute(
            f"SELECT {COLUNAS} FROM lancamento ORDER BY id"
        ).fetchall()
        return [self._reconstituir(linha) for linha in linhas]

    def atualizar(self, lancamento):
        with self._conexao:
            cursor = self._conexao.execute(
                "UPDATE lancamento SET descricao = ?, valor = ?, data = ?, categoria = ? "
                "WHERE id = ?",
                (
                    lancamento.descricao,
                    lancamento.valor,
                    lancamento.data,
                    lancamento.categoria.nome,
                    lancamento.id,
                ),
            )
        if cursor.rowcount == 0:
            raise LancamentoNaoEncontradoError("Lancamento nunca foi adicionado")

    def listar_por_categoria(self, nome):
        linhas = self._conexao.execute(
            f"SELECT {COLUNAS} FROM lancamento WHERE categoria = ? ORDER BY id",
            (nome,),
        ).fetchall()
        return [self._reconstituir(linha) for linha in linhas]

    @staticmethod
    def _reconstituir(linha):
        id, descricao, valor, data, categoria = linha
        lancamento = Lancamento(descricao, valor, data, Categoria(categoria))
        lancamento.atribuir_id(id)
        return lancamento
