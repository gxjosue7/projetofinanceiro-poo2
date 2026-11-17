import sqlite3

from financeiro.categoria import Categoria
from financeiro.esquema_sqlite import criar_esquema
from financeiro.lancamento import Lancamento
from financeiro.repositorio_lancamento_sqlite import RepositorioLancamentoSQLite


def _abrir(caminho):
    conexao = sqlite3.connect(caminho)
    criar_esquema(conexao)
    return RepositorioLancamentoSQLite(conexao), conexao


def _lancamento():
    return Lancamento("Mercado", -150.0, "2026-08-01", Categoria("Alimentacao"))


class TestPersistenciaSQLite:

    def test_os_dados_sobrevivem_ao_reinicio_do_programa(self, tmp_path):
        arquivo = str(tmp_path / "financeiro.db")
        repositorio, conexao = _abrir(arquivo)
        lancamento = _lancamento()
        repositorio.adicionar(lancamento)
        conexao.close()

        repositorio_novo, conexao_nova = _abrir(arquivo)
        relido = repositorio_novo.obter(lancamento.id)
        assert relido.descricao == "Mercado"
        assert relido.valor == -150.0
        assert relido.data == "2026-08-01"
        assert relido.categoria.nome == "Alimentacao"
        conexao_nova.close()

    def test_mudanca_sem_atualizar_nao_e_guardada(self):
        repositorio, _ = _abrir(":memory:")
        lancamento = _lancamento()
        repositorio.adicionar(lancamento)
        lancamento.descricao = "Feira"
        assert repositorio.obter(lancamento.id).descricao == "Mercado"

    def test_cada_leitura_devolve_um_objeto_novo(self):
        repositorio, _ = _abrir(":memory:")
        lancamento = _lancamento()
        repositorio.adicionar(lancamento)
        assert repositorio.obter(lancamento.id) is not lancamento

    def test_listar_mantem_a_ordem_de_insercao(self, tmp_path):
        arquivo = str(tmp_path / "financeiro.db")
        repositorio, conexao = _abrir(arquivo)
        for descricao in ["Primeiro", "Segundo", "Terceiro"]:
            repositorio.adicionar(
                Lancamento(descricao, -10.0, "2026-08-01", Categoria("Lazer"))
            )
        conexao.close()

        repositorio_novo, conexao_nova = _abrir(arquivo)
        descricoes = [l.descricao for l in repositorio_novo.listar()]
        assert descricoes == ["Primeiro", "Segundo", "Terceiro"]
        conexao_nova.close()
