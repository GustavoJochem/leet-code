# Remove Element from Array

Este repositório contém uma implementação da solução para o problema de remoção de todas as ocorrências de um valor específico de um array de inteiros, `nums`. A solução é apresentada em Python.

## Problema

Você é fornecido com um array de inteiros `nums` e um inteiro `val`, e sua tarefa é remover todas as ocorrências de `val` em `nums` in-place. Após a remoção, a ordem dos elementos pode ser alterada. O resultado deve ser armazenado no próprio array `nums`, e você deve retornar o número de elementos que não são iguais a `val`.

### Exemplo

```plaintext
Input: nums = [3, 2, 2, 3], val = 3
Output: 2, nums = [2, 2, _, _]
```

## Solução

A solução utiliza uma abordagem de dois ponteiros para percorrer o array e armazenar os elementos que não são iguais a `val` nas primeiras posições do array. O método percorre todos os elementos e, sempre que encontra um valor diferente de `val`, ele o coloca na posição correta.

### Algoritmo

1. Inicialize a variável `k` como 0, que representará o número de elementos que não são iguais a `val`.
2. Percorra o array `nums` usando um loop:
   - Para cada elemento, verifique se ele é diferente de `val`.
   - Se for diferente, armazene-o na posição `k` e incremente `k`.
3. Após percorrer todos os elementos, retorne `k`, que representa o número de elementos que não são iguais a `val`.

### Código

A implementação da solução está localizada no arquivo `solution.py`.

## Complexidade

- **Complexidade de Tempo**: O(n), onde `n` é o tamanho do array `nums`. Cada elemento é processado uma vez.
- **Complexidade de Espaço**: O(1), pois a remoção é realizada in-place e não utiliza espaço adicional significativo.

## Testes

Os testes para a implementação estão localizados no arquivo `test.py`. O arquivo contém vários cenários de teste que validam a solução, incluindo casos normais, casos onde todos os elementos são iguais a `val`, listas vazias e listas sem o valor a ser removido.

### Como Executar os Testes

1. Certifique-se de que você tenha o Python instalado.
2. Navegue até a pasta onde os arquivos estão localizados.
3. Execute o arquivo de teste usando o seguinte comando:

   ```bash
   python test.py
   ```

Se todos os testes forem bem-sucedidos, você verá a mensagem "Todos os testes passaram!". Caso contrário, a mensagem de erro correspondente será exibida.