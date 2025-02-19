# Remove Duplicates from Sorted Array

Este repositório contém uma implementação da solução para o problema de remover duplicatas de um array de inteiros ordenados, `nums`. A solução é apresentada em Python.

## Problema

Você é fornecido com um array de inteiros `nums` ordenado em ordem não decrescente e sua tarefa é remover as duplicatas in-place, de modo que cada elemento único apareça apenas uma vez. A ordem relativa dos elementos deve ser mantida. Após a remoção, o número de elementos únicos deve ser retornado.

## Exemplo

**Input:** 
```plaintext
nums = [0,0,1,1,1,2,2,3,3,4]
```
**Output:** 
```plaintext
5, nums = [0,1,2,3,4,_,_,_,_,_]
```

## Solução

A solução utiliza uma abordagem de dois ponteiros para percorrer o array e armazenar os elementos únicos nas primeiras posições do array. O método percorre todos os elementos e, sempre que encontra um valor diferente do anterior, ele o coloca na posição correta.

### Algoritmo

1. Inicialize a variável `j` como 1, que representará o índice do próximo elemento único a ser armazenado.
2. Percorra o array `nums` usando um loop a partir do segundo elemento (índice 1):
   - Para cada elemento, verifique se ele é diferente do anterior.
   - Se for diferente, armazene-o na posição `j` e incremente `j`.
3. Após percorrer todos os elementos, retorne `j`, que representa o número de elementos únicos.

## Código

A implementação da solução está localizada no arquivo `solution.py`.

## Complexidade

- **Complexidade de Tempo:** O(n), onde n é o tamanho do array `nums`. Cada elemento é processado uma vez.
- **Complexidade de Espaço:** O(1), pois a remoção é realizada in-place e não utiliza espaço adicional significativo.

## Testes

Os testes para a implementação estão localizados no arquivo `test.py`. O arquivo contém vários cenários de teste que validam a solução, incluindo casos normais, casos onde todos os elementos são iguais, listas vazias e listas sem duplicatas.

## Como Executar os Testes

Certifique-se de que você tenha o Python instalado.

Navegue até a pasta onde os arquivos estão localizados.

Execute o arquivo de teste usando o seguinte comando:

```bash
python test.py
```

Se todos os testes forem bem-sucedidos, você verá a mensagem "Todos os testes passaram!". Caso contrário, a mensagem de erro correspondente será exibida.