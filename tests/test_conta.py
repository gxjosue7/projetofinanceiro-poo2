class TestConta: 
    def __init__(self, nome:str, saldo:float):
        self.nome = nome
        self.saldo = saldo

    def depositar(self, valor:float):
        self.saldo += valor
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.saldo = self.saldo + valor
             
        

