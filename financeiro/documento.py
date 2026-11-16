from abc import ABC, abstractmethod


class Documento(ABC):

    def __init__(self):
        self._linhas = []

    def adicionar_linha(self, campo, valor):
        self._linhas.append((campo, valor))

    @abstractmethod
    def conteudo(self):
        ...

    def salvar(self, caminho):
        with open(caminho, "w", encoding="utf-8") as arquivo:
            arquivo.write(self.conteudo())


class DocumentoCsv(Documento):

    def conteudo(self):
        linhas = ["campo,valor"]
        for campo, valor in self._linhas:
            linhas.append(f"{campo},{valor}")
        return "\n".join(linhas) + "\n"


class DocumentoHtml(Documento):

    def conteudo(self):
        itens = "".join(
            f"<li>{campo}: {valor}</li>" for campo, valor in self._linhas
        )
        return f"<html><body><h1>Extrato</h1><ul>{itens}</ul></body></html>"
