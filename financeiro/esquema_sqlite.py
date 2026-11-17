ESQUEMA = """
CREATE TABLE IF NOT EXISTS lancamento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    valor REAL NOT NULL,
    data TEXT NOT NULL,
    categoria TEXT NOT NULL
);
"""


def criar_esquema(conexao):
    conexao.executescript(ESQUEMA)
