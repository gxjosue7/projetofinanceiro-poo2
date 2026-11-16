import pytest
from financeiro.estrategia_correcao import CorrecaoIpca, CorrecaoSelic, EstrategiaCorrecao


class TestCorrecaoIpca:

    def test_corrige_pelo_percentual_acumulado(self):
        assert CorrecaoIpca(5.0).corrigir(1000.0, 12) == pytest.approx(1050.0)

    def test_percentual_negativo_lanca_erro(self):
        with pytest.raises(ValueError):
            CorrecaoIpca(-1.0)


class TestCorrecaoSelic:

    def test_corrige_pela_taxa_mensal_composta(self):
        assert CorrecaoSelic(1.0).corrigir(1000.0, 2) == pytest.approx(1020.10)

    def test_taxa_negativa_lanca_erro(self):
        with pytest.raises(ValueError):
            CorrecaoSelic(-1.0)


class TestEstrategiaCorrecao:

    def test_interface_nao_pode_ser_instanciada(self):
        with pytest.raises(TypeError):
            EstrategiaCorrecao()
