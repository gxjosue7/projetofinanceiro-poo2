from financeiro.conta import Conta
from financeiro.criador_importador import Banco
from financeiro.importador import Importador
from financeiro.categoria import Categoria
from financeiro.lancamento import Lancamento
from financeiro.servico_importacao import ServicoImportacao


class ImportadorFalso(Importador):

    def importar(self, caminho):
        return [
            Lancamento("Salario", 3000.0, "2026-08-01", Categoria("Renda")),
            Lancamento("Mercado", -300.0, "2026-08-05", Categoria("Alimentacao")),
        ]


class CriadorImportadorFalso:

    def criar(self, banco):
        return ImportadorFalso()


class ExportadorEspiao:

    def __init__(self):
        self.extratos = []

    def exportar(self, extrato, caminho):
        self.extratos.append(extrato)


class TestServicoImportacao:

    def test_importa_registra_na_conta_e_exporta(self):
        exportador = ExportadorEspiao()
        servico = ServicoImportacao(CriadorImportadorFalso(), exportador)
        conta = Conta("Corrente", 1000.0)
        extrato = servico.importar_e_exportar(Banco.ALFA, "qualquer.csv", conta, "2026-08", "saida.csv")
        assert conta.saldo == 3700.0
        assert exportador.extratos == [extrato]
        assert extrato.saldo_final() == 2700.0
