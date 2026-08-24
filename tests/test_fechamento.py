from financeiro.categoria import Categoria
from financeiro.fechamento import Fechamento
from financeiro.lancamento import Lancamento


class TestFechamento:

    def setup_method(self):
        self.categoria = Categoria("Alimentacao")

    def test_fechamento_sem_lancamentos(self):
        fechamento = Fechamento([])
        assert fechamento.total_lancamentos() == 0
        assert fechamento.total_creditos() == 0.0
        assert fechamento.total_debitos() == 0.0
        assert fechamento.saldo() == 0.0

    def test_fechamento_consolida_lancamentos(self):
        lancamentos = [
            Lancamento("Salario", 3000.0, "2026-08-01", self.categoria),
            Lancamento("Mercado", -300.0, "2026-08-05", self.categoria),
            Lancamento("Aluguel", -800.0, "2026-08-10", self.categoria),
        ]
        fechamento = Fechamento(lancamentos)
        assert fechamento.total_lancamentos() == 3
        assert fechamento.total_creditos() == 3000.0
        assert fechamento.total_debitos() == 1100.0
        assert fechamento.saldo() == 1900.0

    def test_fechamento_nao_e_afetado_por_mudanca_na_lista_original(self):
        lancamentos = [Lancamento("Salario", 3000.0, "2026-08-01", self.categoria)]
        fechamento = Fechamento(lancamentos)
        lancamentos.append(Lancamento("Mercado", -300.0, "2026-08-05", self.categoria))
        assert fechamento.total_lancamentos() == 1
