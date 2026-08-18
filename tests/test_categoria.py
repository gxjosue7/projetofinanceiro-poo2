class TestCategoria:
    def __init__(self, alimentação, transporte, moradia, outros):
        self.alimentação = alimentação
        self.transporte = transporte
        self.moradia = moradia
        self.outros = outros
        assert self.alimentação == alimentação
        assert self.transporte == transporte
        assert self.moradia == moradia
        assert self.outros == outros