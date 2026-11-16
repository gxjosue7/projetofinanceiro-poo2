from financeiro.leitor import LeitorCsv, LeitorJson


class CriadorLeitor:

    def criar(self, caminho):
        caminho = str(caminho).lower()
        if caminho.endswith(".csv"):
            return LeitorCsv()
        if caminho.endswith(".json"):
            return LeitorJson()
        raise ValueError(f"Formato de arquivo nao suportado: {caminho}")
