import pytest
from financeiro.composicao import montar_servico_importacao
from financeiro.conta import Conta
from financeiro.criador_importador import Banco


class TestComposicao:

    def _arquivo(self, tmp_path):
        arquivo = tmp_path / "extrato.csv"
        arquivo.write_text(
            "descricao,valor,data,categoria\n"
            "Salario,3000.0,2026-08-01,Renda\n"
            "Mercado,-300.0,2026-08-05,Alimentacao\n",
            encoding="utf-8",
        )
        return arquivo

    def test_fluxo_completo_em_csv(self, tmp_path):
        servico = montar_servico_importacao("csv")
        conta = Conta("Corrente", 1000.0)
        relatorio = tmp_path / "relatorio.csv"
        servico.importar_e_exportar(Banco.ALFA, self._arquivo(tmp_path), conta, "2026-08", relatorio)
        assert conta.saldo == 3700.0
        assert "Saldo final,2700.0" in relatorio.read_text(encoding="utf-8")

    def test_fluxo_completo_em_html(self, tmp_path):
        servico = montar_servico_importacao("html")
        conta = Conta("Corrente", 1000.0)
        relatorio = tmp_path / "relatorio.html"
        servico.importar_e_exportar(Banco.ALFA, self._arquivo(tmp_path), conta, "2026-08", relatorio)
        assert "<li>Saldo final: 2700.0</li>" in relatorio.read_text(encoding="utf-8")

    def test_formato_de_relatorio_desconhecido_lanca_erro(self):
        with pytest.raises(ValueError):
            montar_servico_importacao("pdf")
