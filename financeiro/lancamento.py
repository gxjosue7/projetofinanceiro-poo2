class Lancamento:

    def __init__(self, descricao, valor, data, categoria):
        if valor == 0:
            raise ValueError("Valor do lancamento nao pode ser zero")
        self._id = None
        self.descricao = descricao
        self.valor = valor
        self.data = data
        self.categoria = categoria

    @property
    def id(self):
        return self._id

    def atribuir_id(self, id):
        if self._id is not None:
            raise ValueError("Lancamento ja possui identidade")
        self._id = id
