import pytest
from financeiro.categoria import Categoria
from financeiro.lancamento import Lancamento
from financeiro.repositorio_lancamento import (
    LancamentoNaoEncontradoError,
    RepositorioLancamento,
)
from financeiro.repositorio_lancamento_memoria import RepositorioLancamentoMemoria


@pytest.fixture
def repositorio():
    return RepositorioLancamentoMemoria()


def _lancamento(categoria="Alimentacao"):
    return Lancamento("Mercado", -150.0, "2026-08-01", Categoria(categoria))


class TestRepositorioLancamento:

    def test_interface_nao_pode_ser_instanciada(self):
        with pytest.raises(TypeError):
            RepositorioLancamento()

    def test_adicionar_atribui_identidade(self, repositorio):
        lancamento = _lancamento()
        repositorio.adicionar(lancamento)
        assert lancamento.id is not None

    def test_adicionar_gera_identidades_diferentes(self, repositorio):
        primeiro = _lancamento()
        segundo = _lancamento()
        repositorio.adicionar(primeiro)
        repositorio.adicionar(segundo)
        assert primeiro.id != segundo.id

    def test_obter_devolve_o_lancamento_guardado(self, repositorio):
        lancamento = _lancamento()
        repositorio.adicionar(lancamento)
        assert repositorio.obter(lancamento.id).descricao == "Mercado"

    def test_obter_inexistente_falha(self, repositorio):
        with pytest.raises(LancamentoNaoEncontradoError):
            repositorio.obter(99)

    def test_listar_devolve_todos(self, repositorio):
        repositorio.adicionar(_lancamento())
        repositorio.adicionar(_lancamento())
        assert len(repositorio.listar()) == 2

    def test_listar_sem_lancamentos_devolve_lista_vazia(self, repositorio):
        assert repositorio.listar() == []

    def test_atualizar_registra_a_mudanca(self, repositorio):
        lancamento = _lancamento()
        repositorio.adicionar(lancamento)
        lancamento.descricao = "Feira"
        repositorio.atualizar(lancamento)
        assert repositorio.obter(lancamento.id).descricao == "Feira"

    def test_atualizar_lancamento_nunca_adicionado_falha(self, repositorio):
        with pytest.raises(LancamentoNaoEncontradoError):
            repositorio.atualizar(_lancamento())

    def test_listar_por_categoria_filtra_pelo_nome(self, repositorio):
        repositorio.adicionar(_lancamento("Alimentacao"))
        repositorio.adicionar(_lancamento("Transporte"))
        repositorio.adicionar(_lancamento("Alimentacao"))
        encontrados = repositorio.listar_por_categoria("Alimentacao")
        assert len(encontrados) == 2

    def test_listar_por_categoria_sem_resultado(self, repositorio):
        repositorio.adicionar(_lancamento("Alimentacao"))
        assert repositorio.listar_por_categoria("Lazer") == []
