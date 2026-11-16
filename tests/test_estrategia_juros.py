import pytest
from financeiro.estrategia_juros import EstrategiaJuros, JurosCompostos, JurosSimples


class TestJurosSimples:

    def test_calcula_juros_simples(self):
        assert JurosSimples().calcular(1000.0, 1.0, 3) == 30.0

    def test_meses_negativos_lancam_erro(self):
        with pytest.raises(ValueError):
            JurosSimples().calcular(1000.0, 1.0, -1)


class TestJurosCompostos:

    def test_calcula_juros_compostos(self):
        assert JurosCompostos().calcular(1000.0, 1.0, 2) == pytest.approx(20.10)

    def test_meses_negativos_lancam_erro(self):
        with pytest.raises(ValueError):
            JurosCompostos().calcular(1000.0, 1.0, -1)


class TestEstrategiaJuros:

    def test_interface_nao_pode_ser_instanciada(self):
        with pytest.raises(TypeError):
            EstrategiaJuros()
