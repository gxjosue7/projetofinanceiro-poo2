from financeiro.categoria import Categoria


class TestCategoria:

    def test_cria_categoria_com_nome(self):
        categoria = Categoria("Alimentacao")
        assert categoria.nome == "Alimentacao"
