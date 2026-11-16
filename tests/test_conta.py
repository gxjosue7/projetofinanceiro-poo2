import pytest
from financeiro.categoria import Categoria
from financeiro.conta import Conta
from financeiro.lancamento import Lancamento


class TestConta:

    def setup_method(self):
        self.conta = Conta("Conta Corrente", 1000.0)

    def test_cria_conta_com_atributos(self):
        assert self.conta.nome == "Conta Corrente"
        assert self.conta.saldo == 1000.0

    def test_depositar_valor_valido(self):
        self.conta.depositar(200.0)
        assert self.conta.saldo == 1200.0

    def test_depositar_valor_invalido_zero(self):
        with pytest.raises(ValueError):
            self.conta.depositar(0)

    def test_depositar_valor_invalido_negativo(self):
        with pytest.raises(ValueError):
            self.conta.depositar(-50)

    def test_sacar_valor_valido(self):
        self.conta.sacar(300.0)
        assert self.conta.saldo == 700.0

    def test_sacar_valor_invalido_negativo(self):
        with pytest.raises(ValueError):
            self.conta.sacar(-10)

    def test_sacar_com_saldo_insuficiente(self):
        with pytest.raises(ValueError):
            self.conta.sacar(5000.0)

    def test_registrar_lancamento_altera_o_saldo(self):
        categoria = Categoria("Alimentacao")
        self.conta.registrar_lancamento(Lancamento("Mercado", -300.0, "2026-08-05", categoria))
        assert self.conta.saldo == 700.0

    def test_registrar_lancamento_que_estoura_o_saldo_falha(self):
        categoria = Categoria("Alimentacao")
        with pytest.raises(ValueError):
            self.conta.registrar_lancamento(Lancamento("Carro", -5000.0, "2026-08-05", categoria))

    def test_saldo_nao_pode_ser_alterado_de_fora(self):
        with pytest.raises(AttributeError):
            self.conta.saldo = 99999