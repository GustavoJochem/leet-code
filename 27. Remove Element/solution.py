from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Inicializamos 'k' como 0, que representará o número de elementos que não são iguais a 'val'
        k = 0

        # Percorremos cada índice 'i' da lista 'nums'
        for i in range(len(nums)):
            # Se o elemento na posição 'i' não for igual a 'val'
            if nums[i] != val:
                # Atribuímos o valor de nums[i] à posição 'k'
                nums[k] = nums[i]
                # Incrementamos 'k' para a próxima posição
                k += 1

        # Retornamos o número de elementos que não são iguais a 'val'
        return k

