class Lancamento:

    def __init__(self, descricao, valor, data, categoria):
        if valor == 0:
            raise ValueError("Valor do lancamento nao pode ser zero")
        self.descricao = descricao
        self.valor = valor
        self.data = data
        self.categoria = categoria