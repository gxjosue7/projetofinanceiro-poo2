from abc import ABC, abstractmethod

from financeiro.documento import DocumentoCsv, DocumentoHtml


class ExportadorRelatorio(ABC):

    def exportar(self, extrato, caminho):
        documento = self.criar_documento()
        documento.adicionar_linha("Periodo", extrato.periodo)
        documento.adicionar_linha("Total de lancamentos", extrato.total_lancamentos())
        documento.adicionar_linha("Total de creditos", extrato.total_creditos())
        documento.adicionar_linha("Total de debitos", extrato.total_debitos())
        documento.adicionar_linha("Saldo final", extrato.saldo_final())
        documento.salvar(caminho)
        return documento

    @abstractmethod
    def criar_documento(self):
        ...


class ExportadorCsv(ExportadorRelatorio):

    def criar_documento(self):
        return DocumentoCsv()


class ExportadorHtml(ExportadorRelatorio):

    def criar_documento(self):
        return DocumentoHtml()
