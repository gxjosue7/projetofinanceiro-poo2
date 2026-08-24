# Sistema de Controle Financeiro Pessoal

Projeto desenvolvido seguindo a mesma evolução aplicada ao E-Commerce nos Módulos 1 e 2 da disciplina.

## Classes

- `Conta` — nome, saldo, com `depositar` e `sacar`
- `Categoria` — nome
- `Lancamento` — descrição, valor, data, categoria
- `Fechamento` — consolida os lançamentos de um período
- `Conciliacao` — verifica se débitos e créditos batem
- `Extrato` — resume os fechamentos de um período

Um `Lancamento` usa o valor com sinal para indicar sua natureza: valor positivo é um crédito (entrada), valor negativo é um débito (saída). É a forma mais simples de diferenciar os dois sem criar um atributo `tipo` a mais.

## Decisões de projeto

**No `Fechamento`, os lançamentos originais foram copiados ou referenciados?**

Os objetos `Lancamento` são referenciados (não são clonados), mas a lista é copiada na criação do `Fechamento` e também sempre que `lancamentos` é acessado. Isso é a mesma solução usada em `Pedido.itens` no E-Commerce: guardar uma cópia da lista impede que alguém adicione ou remova lançamentos de um fechamento já feito mexendo na lista original por fora, mas não faz sentido duplicar os `Lancamento` em si, já que um fechamento só resume lançamentos que continuam existindo no sistema.

**`Conciliacao` virou uma classe própria ou um método de `Fechamento`?**

Classe própria. Um `Fechamento` resume lançamentos de uma única lista; a `Conciliacao` compara dois conjuntos diferentes (débitos e créditos) para checar se batem. São responsabilidades diferentes, assim como `Pagamento` no E-Commerce não é um método de `Pedido`, e sim uma classe separada que o `Pedido` usa.

**O que acontece quando não há lançamentos no período, ou quando a conciliação não bate?**

- Um `Fechamento` sem lançamentos não é erro: retorna totais zerados. Um período sem movimentação é uma informação válida, não uma falha (diferente do `Carrinho.finalizar()` do E-Commerce, que lança erro porque um pedido vazio não faz sentido finalizar).
- Uma `Conciliacao` que não bate pode ser consultada sem erro pelo método `esta_conciliada()`, que devolve `True` ou `False`. Já o método `verificar()` lança `ValueError` com o valor dos dois lados quando os totais não conferem, para quem precisa que a conciliação seja obrigatória.

## Extrato e conciliação pendente

`Extrato` recebe um período, uma lista de `Fechamento` e, opcionalmente, uma lista de `Conciliacao`. Ele soma os totais de todos os fechamentos do período (`total_lancamentos`, `total_creditos`, `total_debitos`, `saldo_final`) e usa `possui_conciliacao_pendente()` para checar se alguma das conciliações informadas não bateu.

## Rodando os testes

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -v
```
