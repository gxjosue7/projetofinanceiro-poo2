import sqlite3

from financeiro.criador_importador import CriadorImportador
from financeiro.criador_leitor import CriadorLeitor
from financeiro.esquema_sqlite import criar_esquema
from financeiro.exportador_relatorio import ExportadorCsv, ExportadorHtml
from financeiro.repositorio_lancamento_memoria import RepositorioLancamentoMemoria
from financeiro.repositorio_lancamento_sqlite import RepositorioLancamentoSQLite
from financeiro.servico_importacao import ServicoImportacao


def montar_servico_importacao(
    formato_relatorio="csv", armazenamento="memoria", caminho_banco=":memory:"
):
    if formato_relatorio == "csv":
        exportador = ExportadorCsv()
    elif formato_relatorio == "html":
        exportador = ExportadorHtml()
    else:
        raise ValueError(f"Formato de relatorio desconhecido: {formato_relatorio}")
    if armazenamento == "memoria":
        repositorio_lancamento = RepositorioLancamentoMemoria()
    elif armazenamento == "sqlite":
        conexao = sqlite3.connect(caminho_banco)
        criar_esquema(conexao)
        repositorio_lancamento = RepositorioLancamentoSQLite(conexao)
    else:
        raise ValueError(f"Armazenamento desconhecido: {armazenamento}")
    criador_importador = CriadorImportador(CriadorLeitor())
    return ServicoImportacao(criador_importador, exportador, repositorio_lancamento)
