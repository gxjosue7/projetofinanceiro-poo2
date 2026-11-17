from financeiro.extrato import Extrato
from financeiro.fechamento import Fechamento


class ServicoImportacao:

    def __init__(self, criador_importador, exportador, repositorio_lancamento):
        self._criador_importador = criador_importador
        self._exportador = exportador
        self._repositorio_lancamento = repositorio_lancamento

    def importar_e_exportar(self, banco, arquivo, conta, periodo, relatorio):
        importador = self._criador_importador.criar(banco)
        lancamentos = importador.importar(arquivo)
        for lancamento in lancamentos:
            conta.registrar_lancamento(lancamento)
            self._repositorio_lancamento.adicionar(lancamento)
        extrato = Extrato(periodo, [Fechamento(lancamentos)])
        self._exportador.exportar(extrato, relatorio)
        return extrato
