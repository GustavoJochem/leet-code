from typing import List
from solution import Solution

def test_removeElement():
    solution = Solution()

    # Teste 1: Caso normal
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = solution.removeElement(nums1, val1)
    assert k1 == 2, f"Erro: Esperado 2, mas obteve {k1}"
    assert sorted(nums1[:k1]) == [2, 2], f"Erro: Esperado [2, 2], mas obteve {nums1[:k1]}"

    # Teste 2: Caso com múltiplas ocorrências
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = solution.removeElement(nums2, val2)
    assert k2 == 5, f"Erro: Esperado 5, mas obteve {k2}"
    assert sorted(nums2[:k2]) == [0, 0, 1, 3, 4], f"Erro: Esperado [0, 0, 1, 3, 4], mas obteve {nums2[:k2]}"

    # Teste 3: Caso onde todos os elementos são iguais a val
    nums3 = [2, 2, 2, 2]
    val3 = 2
    k3 = solution.removeElement(nums3, val3)
    assert k3 == 0, f"Erro: Esperado 0, mas obteve {k3}"
    assert nums3[:k3] == [], f"Erro: Esperado [], mas obteve {nums3[:k3]}"

    # Teste 4: Caso onde não há elementos a remover
    nums4 = [1, 2, 3, 4]
    val4 = 5
    k4 = solution.removeElement(nums4, val4)
    assert k4 == 4, f"Erro: Esperado 4, mas obteve {k4}"
    assert sorted(nums4[:k4]) == [1, 2, 3, 4], f"Erro: Esperado [1, 2, 3, 4], mas obteve {nums4[:k4]}"

    # Teste 5: Caso de lista vazia
    nums5 = []
    val5 = 1
    k5 = solution.removeElement(nums5, val5)
    assert k5 == 0, f"Erro: Esperado 0, mas obteve {k5}"
    assert nums5[:k5] == [], f"Erro: Esperado [], mas obteve {nums5[:k5]}"

    # Teste 6: Caso com valores no limite
    nums6 = [1] * 100  # Lista com 100 elementos, todos iguais a 1
    val6 = 1
    k6 = solution.removeElement(nums6, val6)
    assert k6 == 0, f"Erro: Esperado 0, mas obteve {k6}"
    assert nums6[:k6] == [], f"Erro: Esperado [], mas obteve {nums6[:k6]}"

    print("Todos os testes passaram!")

# Chama a função de teste
if __name__ == "__main__":
    test_removeElement()