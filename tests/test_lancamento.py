import pytest
from financeiro.categoria import Categoria
from financeiro.lancamento import Lancamento


class TestLancamento:

    def setup_method(self):
        self.categoria = Categoria("Alimentacao")

    def test_cria_lancamento_com_atributos(self):
        lancamento = Lancamento("Mercado", -150.0, "2026-08-01", self.categoria)
        assert lancamento.descricao == "Mercado"
        assert lancamento.valor == -150.0
        assert lancamento.data == "2026-08-01"
        assert lancamento.categoria is self.categoria

    def test_valor_zero_lanca_erro(self):
        with pytest.raises(ValueError):
            Lancamento("Mercado", 0, "2026-08-01", self.categoria)