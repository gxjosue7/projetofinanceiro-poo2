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

## Ajustes após o feedback

A `Conta` agora guarda a lista de lançamentos e calcula o `saldo` a partir do saldo inicial somado aos lançamentos, em vez de guardar um número solto. O `saldo` é somente leitura. `depositar` e `sacar` passaram a registrar lançamentos, então o saldo nunca fica fora de sincronia. A regra de saldo insuficiente passou para `registrar_lancamento`. O `Lancamento` recusa valor zero. A `Conciliacao` passou a inverter o sinal dos débitos, que são negativos pela convenção deste projeto.

## Estratégias

`EstrategiaRendimento` (poupança e CDB pré-fixado), `EstrategiaJuros` (simples e compostos) e `EstrategiaCorrecao` (IPCA e Selic) seguem o padrão Strategy. A `Aplicacao` usa a estratégia de rendimento.

**Rendimento, juros e correção monetária são interfaces separadas ou a mesma reaproveitada? Por quê?**

Separadas. Cada uma responde uma pergunta diferente e recebe entradas diferentes: o rendimento recebe só o valor aplicado, os juros recebem capital, taxa e meses, e a correção recebe o valor e os meses. Juntar tudo em uma interface obrigaria parâmetros que algumas implementações não usam. Reaproveitar uma interface só faz sentido quando o comportamento é realmente o mesmo, como o Cupom reaproveitando a estratégia de desconto.

**Onde a estratégia escolhida é guardada?**

A `Aplicacao` guarda a estratégia de rendimento como atributo, porque a regra de um investimento é combinada na contratação e não muda depois, como o Cupom guardado no Pedido. Juros e correção não têm uma entidade que as guarde ainda: quem chama passa os valores e a estratégia é usada direto.

**Que novo tipo de regra eu conseguiria adicionar hoje sem editar nenhuma classe existente?**

Um novo investimento (por exemplo uma LCI) é uma nova classe que implementa `EstrategiaRendimento`. Do mesmo jeito, um novo tipo de juros ou de correção é uma nova classe. Nenhuma classe existente muda (Open/Closed).

## Criação de objetos e injeção de dependências

Os leitores (`LeitorCsv`, `LeitorJson`), importadores por banco (`ImportadorBancoAlfa`, `ImportadorBancoBeta`) e exportadores de relatório (`ExportadorCsv`, `ExportadorHtml`) são criados por factories. O `ServicoImportacao` lê o arquivo, registra os lançamentos na conta, monta o extrato e exporta o relatório. A montagem está em `composicao.py`.

**Em cada caso (leitor, importador, exportador), Simple Factory ou Factory Method? O que fez escolher?**

Leitor: Simple Factory (`CriadorLeitor`), porque a escolha depende de um dado simples, a extensão do arquivo. Importador: Simple Factory (`CriadorImportador`), porque a escolha depende de um dado, o banco de origem (enum `Banco`). Exportador: Factory Method, porque `ExportadorRelatorio.exportar` descreve o fluxo comum do relatório e cada subclasse decide qual documento criar em `criar_documento`, já que cada formato monta o documento de um jeito diferente.

**Nos serviços, o que é injetado e o que ainda é criado internamente?**

O `ServicoImportacao` recebe o `CriadorImportador` e o exportador pelo construtor. O `CriadorImportador` e os importadores recebem o `CriadorLeitor`. Ainda são criados internamente o `Fechamento` e o `Extrato` dentro do serviço, porque são objetos do domínio feitos para aquela operação e não precisam ser trocados, e os documentos, criados pelo próprio exportador.

**Onde está a raiz de composição? Que colaborador seria substituível hoje sem editar nenhum serviço?**

Em `financeiro/composicao.py`, na função `montar_servico_importacao`, único lugar que cria as peças reais. Dá para trocar o exportador (CSV por HTML) mudando só o parâmetro, e os testes de `test_servico_importacao.py` substituem o criador de importadores e o exportador por dublês sem editar o serviço.
