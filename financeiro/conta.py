class Conta:

    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor do deposito deve ser positivo")
        self.saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor do saque deve ser positivo")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= valor
