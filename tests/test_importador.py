import pytest
from financeiro.criador_importador import Banco, CriadorImportador
from financeiro.criador_leitor import CriadorLeitor
from financeiro.importador import ImportadorBancoAlfa, ImportadorBancoBeta


class TestImportador:

    def setup_method(self):
        self.criador = CriadorImportador(CriadorLeitor())

    def _arquivo(self, tmp_path):
        arquivo = tmp_path / "extrato.csv"
        arquivo.write_text(
            "descricao,valor,data,categoria\nMercado,-300.0,2026-08-05,Alimentacao\n",
            encoding="utf-8",
        )
        return arquivo

    def test_cria_importador_do_banco_alfa(self):
        assert isinstance(self.criador.criar(Banco.ALFA), ImportadorBancoAlfa)

    def test_cria_importador_do_banco_beta(self):
        assert isinstance(self.criador.criar(Banco.BETA), ImportadorBancoBeta)

    def test_banco_desconhecido_lanca_erro(self):
        with pytest.raises(ValueError):
            self.criador.criar("alfa")

    def test_banco_alfa_mantem_os_valores(self, tmp_path):
        lancamentos = self.criador.criar(Banco.ALFA).importar(self._arquivo(tmp_path))
        assert lancamentos[0].valor == -300.0

    def test_banco_beta_inverte_o_sinal(self, tmp_path):
        lancamentos = self.criador.criar(Banco.BETA).importar(self._arquivo(tmp_path))
        assert lancamentos[0].valor == 300.0
