class Fechamento:

    def __init__(self, lancamentos):
        self._lancamentos = list(lancamentos)

    @property
    def lancamentos(self):
        return list(self._lancamentos)

    def total_lancamentos(self):
        return len(self._lancamentos)

    def total_creditos(self):
        return sum(l.valor for l in self._lancamentos if l.valor > 0)

    def total_debitos(self):
        return sum(-l.valor for l in self._lancamentos if l.valor < 0)

    def saldo(self):
        return sum(l.valor for l in self._lancamentos)
