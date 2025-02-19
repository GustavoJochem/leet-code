from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Inicializa 'j' como 1, que será usado para rastrear a posição do próximo elemento único
        j = 1

        # Itera através do array a partir do segundo elemento (índice 1)
        for i in range(1, len(nums)):
            # Verifica se o elemento atual é diferente do anterior
            if nums[i] != nums[i - 1]:
                # Se for diferente, significa que encontramos um novo elemento único
                # Coloca o novo elemento na posição 'j'
                nums[j] = nums[i]
                # Incrementa 'j' para a próxima posição de escrita
                j += 1

        # Retorna o número de elementos únicos encontrados
        return j