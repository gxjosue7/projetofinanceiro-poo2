import pytest
from financeiro.categoria import Categoria
from financeiro.documento import Documento, DocumentoCsv, DocumentoHtml
from financeiro.exportador_relatorio import ExportadorCsv, ExportadorHtml, ExportadorRelatorio
from financeiro.extrato import Extrato
from financeiro.fechamento import Fechamento
from financeiro.lancamento import Lancamento


class TestExportadorRelatorio:

    def setup_method(self):
        categoria = Categoria("Alimentacao")
        fechamento = Fechamento([
            Lancamento("Salario", 3000.0, "2026-08-01", categoria),
            Lancamento("Mercado", -300.0, "2026-08-05", categoria),
        ])
        self.extrato = Extrato("2026-08", [fechamento])

    def test_exportador_csv_cria_documento_csv(self):
        assert isinstance(ExportadorCsv().criar_documento(), DocumentoCsv)

    def test_exportador_html_cria_documento_html(self):
        assert isinstance(ExportadorHtml().criar_documento(), DocumentoHtml)

    def test_exporta_csv_com_o_resumo_do_extrato(self, tmp_path):
        arquivo = tmp_path / "relatorio.csv"
        ExportadorCsv().exportar(self.extrato, arquivo)
        texto = arquivo.read_text(encoding="utf-8")
        assert "Periodo,2026-08" in texto
        assert "Saldo final,2700.0" in texto

    def test_exporta_html_com_o_resumo_do_extrato(self, tmp_path):
        arquivo = tmp_path / "relatorio.html"
        ExportadorHtml().exportar(self.extrato, arquivo)
        texto = arquivo.read_text(encoding="utf-8")
        assert "<li>Saldo final: 2700.0</li>" in texto

    def test_exportador_nao_pode_ser_instanciado(self):
        with pytest.raises(TypeError):
            ExportadorRelatorio()

    def test_documento_nao_pode_ser_instanciado(self):
        with pytest.raises(TypeError):
            Documento()
