class Extrato:

    def __init__(self, periodo, fechamentos, conciliacoes=None):
        self.periodo = periodo
        self._fechamentos = list(fechamentos)
        self._conciliacoes = list(conciliacoes) if conciliacoes else []

    @property
    def fechamentos(self):
        return list(self._fechamentos)

    def total_lancamentos(self):
        return sum(f.total_lancamentos() for f in self._fechamentos)

    def total_creditos(self):
        return sum(f.total_creditos() for f in self._fechamentos)

    def total_debitos(self):
        return sum(f.total_debitos() for f in self._fechamentos)

    def saldo_final(self):
        return sum(f.saldo() for f in self._fechamentos)

    def possui_conciliacao_pendente(self):
        return any(not c.esta_conciliada() for c in self._conciliacoes)
