import sqlite3

import pytest
from financeiro.esquema_sqlite import criar_esquema
from financeiro.repositorio_lancamento_memoria import RepositorioLancamentoMemoria
from financeiro.repositorio_lancamento_sqlite import RepositorioLancamentoSQLite


@pytest.fixture(params=["memoria", "sqlite"])
def repositorio(request):
    if request.param == "memoria":
        return RepositorioLancamentoMemoria()
    conexao = sqlite3.connect(":memory:")
    criar_esquema(conexao)
    return RepositorioLancamentoSQLite(conexao)
