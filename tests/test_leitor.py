import pytest
from financeiro.criador_leitor import CriadorLeitor
from financeiro.leitor import Leitor, LeitorCsv, LeitorJson


class TestLeitorCsv:

    def test_le_lancamentos_do_arquivo(self, tmp_path):
        arquivo = tmp_path / "extrato.csv"
        arquivo.write_text(
            "descricao,valor,data,categoria\n"
            "Salario,3000.0,2026-08-01,Renda\n"
            "Mercado,-300.0,2026-08-05,Alimentacao\n",
            encoding="utf-8",
        )
        lancamentos = LeitorCsv().ler(arquivo)
        assert len(lancamentos) == 2
        assert lancamentos[0].descricao == "Salario"
        assert lancamentos[1].valor == -300.0
        assert lancamentos[1].categoria.nome == "Alimentacao"


class TestLeitorJson:

    def test_le_lancamentos_do_arquivo(self, tmp_path):
        arquivo = tmp_path / "extrato.json"
        arquivo.write_text(
            '[{"descricao": "Salario", "valor": 3000.0, "data": "2026-08-01", "categoria": "Renda"}]',
            encoding="utf-8",
        )
        lancamentos = LeitorJson().ler(arquivo)
        assert len(lancamentos) == 1
        assert lancamentos[0].valor == 3000.0


class TestLeitor:

    def test_interface_nao_pode_ser_instanciada(self):
        with pytest.raises(TypeError):
            Leitor()


class TestCriadorLeitor:

    def test_cria_leitor_csv(self):
        assert isinstance(CriadorLeitor().criar("extrato.csv"), LeitorCsv)

    def test_cria_leitor_json(self):
        assert isinstance(CriadorLeitor().criar("extrato.json"), LeitorJson)

    def test_formato_desconhecido_lanca_erro(self):
        with pytest.raises(ValueError):
            CriadorLeitor().criar("extrato.pdf")
