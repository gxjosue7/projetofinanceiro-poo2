import pytest
from financeiro.estrategia_rendimento import (
    EstrategiaRendimento,
    RendimentoCdbPrefixado,
    RendimentoPoupanca,
)


class TestRendimentoPoupanca:

    def test_rende_meio_por_cento_ao_mes(self):
        assert RendimentoPoupanca().calcular(1000.0) == 5.0


class TestRendimentoCdbPrefixado:

    def test_rende_conforme_a_taxa_combinada(self):
        assert RendimentoCdbPrefixado(1.0).calcular(1000.0) == 10.0

    def test_percentual_negativo_lanca_erro(self):
        with pytest.raises(ValueError):
            RendimentoCdbPrefixado(-1.0)


class TestEstrategiaRendimento:

    def test_interface_nao_pode_ser_instanciada(self):
        with pytest.raises(TypeError):
            EstrategiaRendimento()
