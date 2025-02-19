from typing import List
from solution import Solution

def test_remove_duplicates():
    solution = Solution()

    # Teste 1: Caso básico
    nums = [1, 1, 2]
    expectedNums = [1, 2]
    k = solution.removeDuplicates(nums)
    assert k == len(expectedNums), f"Erro: esperado {len(expectedNums)}, mas obteve {k}"
    for i in range(k):
        assert nums[i] == expectedNums[i], f"Erro: esperado {expectedNums[i]} na posição {i}, mas obteve {nums[i]}"

     # Teste 2: Todos os elementos são iguais
    nums = [5, 5, 5, 5, 5]
    expectedNums = [5]
    k = solution.removeDuplicates(nums)
    assert k == len(expectedNums), f"Erro: esperado {len(expectedNums)}, mas obteve {k}"
    for i in range(k):
        assert nums[i] == expectedNums[i], f"Erro: esperado {expectedNums[i]} na posição {i}, mas obteve {nums[i]}"

    # Teste 3: Nenhum elemento repetido
    nums = [1, 2, 3, 4, 5]
    expectedNums = [1, 2, 3, 4, 5]
    k = solution.removeDuplicates(nums)
    assert k == len(expectedNums), f"Erro: esperado {len(expectedNums)}, mas obteve {k}"
    for i in range(k):
        assert nums[i] == expectedNums[i], f"Erro: esperado {expectedNums[i]} na posição {i}, mas obteve {nums[i]}"

    # Teste 4: Elementos intercalados
    nums = [0, 0, 1, 1, 2, 3, 3, 4]
    expectedNums = [0, 1, 2, 3, 4]
    k = solution.removeDuplicates(nums)
    assert k == len(expectedNums), f"Erro: esperado {len(expectedNums)}, mas obteve {k}"
    for i in range(k):
        assert nums[i] == expectedNums[i], f"Erro: esperado {expectedNums[i]} na posição {i}, mas obteve {nums[i]}"

    # Teste 5: Vários elementos repetidos
    nums = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6]
    expectedNums = [1, 2, 3, 4, 5, 6]
    k = solution.removeDuplicates(nums)
    assert k == len(expectedNums), f"Erro: esperado {len(expectedNums)}, mas obteve {k}"
    for i in range(k):
        assert nums[i] == expectedNums[i], f"Erro: esperado {expectedNums[i]} na posição {i}, mas obteve {nums[i]}"

    # Teste 7: Lista com um único elemento
    nums = [1]
    expectedNums = [1]
    k = solution.removeDuplicates(nums)
    assert k == len(expectedNums), f"Erro: esperado {len(expectedNums)}, mas obteve {k}"
    for i in range(k):
        assert nums[i] == expectedNums[i], f"Erro: esperado {expectedNums[i]} na posição {i}, mas obteve {nums[i]}"

    # Teste 8: Lista com elementos negativos e positivos
    nums = [-3, -3, -2, -1, 0, 1, 1, 2]
    expectedNums = [-3, -2, -1, 0, 1, 2]
    k = solution.removeDuplicates(nums)
    assert k == len(expectedNums), f"Erro: esperado {len(expectedNums)}, mas obteve {k}"
    for i in range(k):
        assert nums[i] == expectedNums[i], f"Erro: esperado {expectedNums[i]} na posição {i}, mas obteve {nums[i]}"

    print("Todos os testes passaram!")

# Chama a função de teste
if __name__ == "__main__":
    test_remove_duplicates()