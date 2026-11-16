import csv
import json
from abc import ABC, abstractmethod

from financeiro.categoria import Categoria
from financeiro.lancamento import Lancamento


class Leitor(ABC):

    @abstractmethod
    def ler(self, caminho):
        ...


class LeitorCsv(Leitor):

    def ler(self, caminho):
        lancamentos = []
        with open(caminho, newline="", encoding="utf-8") as arquivo:
            for linha in csv.DictReader(arquivo):
                lancamentos.append(
                    Lancamento(
                        linha["descricao"],
                        float(linha["valor"]),
                        linha["data"],
                        Categoria(linha["categoria"]),
                    )
                )
        return lancamentos


class LeitorJson(Leitor):

    def ler(self, caminho):
        with open(caminho, encoding="utf-8") as arquivo:
            registros = json.load(arquivo)
        return [
            Lancamento(
                r["descricao"],
                float(r["valor"]),
                r["data"],
                Categoria(r["categoria"]),
            )
            for r in registros
        ]
