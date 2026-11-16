from financeiro.categoria import Categoria
from financeiro.conciliacao import Conciliacao
from financeiro.extrato import Extrato
from financeiro.fechamento import Fechamento
from financeiro.lancamento import Lancamento


class TestExtrato:

    def setup_method(self):
        self.categoria = Categoria("Alimentacao")

    def test_extrato_consolida_fechamentos(self):
        fechamento1 = Fechamento([Lancamento("Salario", 3000.0, "2026-08-01", self.categoria)])
        fechamento2 = Fechamento([Lancamento("Mercado", -300.0, "2026-08-05", self.categoria)])
        extrato = Extrato("Agosto/2026", [fechamento1, fechamento2])

        assert extrato.total_lancamentos() == 2
        assert extrato.total_creditos() == 3000.0
        assert extrato.total_debitos() == 300.0
        assert extrato.saldo_final() == 2700.0

    def test_extrato_sem_fechamentos(self):
        extrato = Extrato("Agosto/2026", [])
        assert extrato.total_lancamentos() == 0
        assert extrato.saldo_final() == 0.0

    def test_extrato_sem_conciliacao_pendente(self):
        debitos = [Lancamento("Saida", -500.0, "2026-08-01", self.categoria)]
        creditos = [Lancamento("Entrada", 500.0, "2026-08-01", self.categoria)]
        conciliacao = Conciliacao(debitos, creditos)
        extrato = Extrato("Agosto/2026", [], [conciliacao])
        assert extrato.possui_conciliacao_pendente() is False

    def test_extrato_com_conciliacao_pendente(self):
        debitos = [Lancamento("Saida", 500.0, "2026-08-01", self.categoria)]
        creditos = [Lancamento("Entrada", 300.0, "2026-08-01", self.categoria)]
        conciliacao = Conciliacao(debitos, creditos)
        extrato = Extrato("Agosto/2026", [], [conciliacao])
        assert extrato.possui_conciliacao_pendente() is True
