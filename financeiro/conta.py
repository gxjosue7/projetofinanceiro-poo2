class Conta: 
    def __init__(self, nome:str, saldo:float):
        self.nome = nome
        self.saldo = saldo
        print(f'Conta {self.nome} criada com saldo inicial de R${self.saldo:.2f}')

