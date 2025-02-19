from typing import List
from solution import Solution

def test_merge():
    solution = Solution()

    # Teste 1: Caso básico
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6], f"Erro: {nums1}"

    # Teste 2: nums2 vazio
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1], f"Erro: {nums1}"

    # Teste 3: nums1 vazio
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1], f"Erro: {nums1}"

    # Teste 4: Elementos iguais
    nums1 = [1, 1, 1, 0, 0, 0]
    m = 3
    nums2 = [1, 1, 1]
    n = 3
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1, 1, 1, 1, 1, 1], f"Erro: {nums1}"

    # Teste 5: Elementos em ordem inversa
    nums1 = [4, 5, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 3, 4, 5, 6], f"Erro: {nums1}"

    # Teste 6: Todas as entradas negativas
    nums1 = [-1, 0, 1, 0, 0, 0]
    m = 3
    nums2 = [-2, -1, 0]
    n = 3
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [-2, -1, -1, 0, 0, 1], f"Erro: {nums1}"

    # Teste 7: Arrays grandes
    nums1 = list(range(1, 201)) + [0] * 100  # nums1 com 200 elementos, os últimos 100 são 0
    m = 200
    nums2 = list(range(201, 301))  # nums2 com 100 elementos
    n = 100
    solution.merge(nums1, m, nums2, n)
    assert nums1 == list(range(1, 301)), f"Erro: {nums1}"

    print("Todos os testes passaram!")

# Chama a função de teste
if __name__ == "__main__":
    test_merge()