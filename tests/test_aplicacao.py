import pytest
from financeiro.aplicacao import Aplicacao
from financeiro.estrategia_rendimento import RendimentoCdbPrefixado, RendimentoPoupanca


class TestAplicacao:

    def test_calcula_rendimento_da_poupanca(self):
        aplicacao = Aplicacao("Reserva", 1000.0, RendimentoPoupanca())
        assert aplicacao.calcular_rendimento() == 5.0

    def test_calcula_rendimento_do_cdb(self):
        aplicacao = Aplicacao("CDB", 1000.0, RendimentoCdbPrefixado(1.0))
        assert aplicacao.calcular_rendimento() == 10.0

    def test_calcula_valor_final(self):
        aplicacao = Aplicacao("CDB", 1000.0, RendimentoCdbPrefixado(1.0))
        assert aplicacao.calcular_valor_final() == 1010.0

    def test_valor_invalido_lanca_erro(self):
        with pytest.raises(ValueError):
            Aplicacao("CDB", 0, RendimentoPoupanca())
