import pytest
from financeiro.categoria import Categoria
from financeiro.conciliacao import Conciliacao
from financeiro.lancamento import Lancamento


class TestConciliacao:

    def setup_method(self):
        self.categoria = Categoria("Transferencia")

    def test_conciliacao_bate(self):
        debitos = [Lancamento("Saida", 500.0, "2026-08-01", self.categoria)]
        creditos = [Lancamento("Entrada", 500.0, "2026-08-01", self.categoria)]
        conciliacao = Conciliacao(debitos, creditos)
        assert conciliacao.esta_conciliada() is True
        conciliacao.verificar()

    def test_conciliacao_nao_bate(self):
        debitos = [Lancamento("Saida", 500.0, "2026-08-01", self.categoria)]
        creditos = [Lancamento("Entrada", 300.0, "2026-08-01", self.categoria)]
        conciliacao = Conciliacao(debitos, creditos)
        assert conciliacao.esta_conciliada() is False

    def test_verificar_lanca_erro_quando_nao_bate(self):
        debitos = [Lancamento("Saida", 500.0, "2026-08-01", self.categoria)]
        creditos = [Lancamento("Entrada", 300.0, "2026-08-01", self.categoria)]
        conciliacao = Conciliacao(debitos, creditos)
        with pytest.raises(ValueError):
            conciliacao.verificar()

    def test_conciliacao_sem_lancamentos_bate(self):
        conciliacao = Conciliacao([], [])
        assert conciliacao.esta_conciliada() is True
