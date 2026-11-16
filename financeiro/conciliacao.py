class Conciliacao:

    def __init__(self, debitos, creditos):
        self._debitos = list(debitos)
        self._creditos = list(creditos)

    def total_debitos(self):
        return sum(-l.valor for l in self._debitos)

    def total_creditos(self):
        return sum(l.valor for l in self._creditos)

    def esta_conciliada(self):
        return self.total_debitos() == self.total_creditos()

    def verificar(self):
        if not self.esta_conciliada():
            raise ValueError(
                f"Conciliacao nao bate: debitos R${self.total_debitos():.2f}, creditos R${self.total_creditos():.2f}"
            )