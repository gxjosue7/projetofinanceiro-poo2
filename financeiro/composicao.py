from financeiro.criador_importador import CriadorImportador
from financeiro.criador_leitor import CriadorLeitor
from financeiro.exportador_relatorio import ExportadorCsv, ExportadorHtml
from financeiro.repositorio_lancamento_memoria import RepositorioLancamentoMemoria
from financeiro.servico_importacao import ServicoImportacao


def montar_servico_importacao(formato_relatorio="csv"):
    if formato_relatorio == "csv":
        exportador = ExportadorCsv()
    elif formato_relatorio == "html":
        exportador = ExportadorHtml()
    else:
        raise ValueError(f"Formato de relatorio desconhecido: {formato_relatorio}")
    criador_importador = CriadorImportador(CriadorLeitor())
    repositorio_lancamento = RepositorioLancamentoMemoria()
    return ServicoImportacao(criador_importador, exportador, repositorio_lancamento)
