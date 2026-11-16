from datetime import date

from financeiro.categoria import Categoria
from financeiro.lancamento import Lancamento


class Conta:

    def __init__(self, nome, saldo):
        self.nome = nome
        self._saldo_inicial = saldo
        self._lancamentos = []

    @property
    def saldo(self):
        return self._saldo_inicial + sum(l.valor for l in self._lancamentos)

    @property
    def lancamentos(self):
        return list(self._lancamentos)

    def registrar_lancamento(self, lancamento):
        if self.saldo + lancamento.valor < 0:
            raise ValueError("Saldo insuficiente")
        self._lancamentos.append(lancamento)

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor do deposito deve ser positivo")
        self.registrar_lancamento(
            Lancamento("Deposito", valor, date.today(), Categoria("Deposito"))
        )

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor do saque deve ser positivo")
        self.registrar_lancamento(
            Lancamento("Saque", -valor, date.today(), Categoria("Saque"))
        )