## Implementação em Python da Estrutura de Dados: Heap (máximo)
### Tarefa proposta para a disciplina de Estrutura de Dados

Para compactuar com a idéia de um heap ter seu primeiro indíce na posição um, algumas adaptações foram feitas:
- O programa inicia uma lista onde sua posição zero é ocupada pelo elemento 0. Os comandos estão programados para ignorarem a posição zero, ou seja, tudo é feito a partir da posição um.
- `n = len(v) - 1` define a quantidade de elementos ou a última posição da Heap ao substrair uma unidade da quantidade de posições que a lista possui (ou seja, ignora a posição zero).
- Para que a posição zero nao apareça para o usuário, será printado a lista a partir da primeira posição: `print(v[1:])`
