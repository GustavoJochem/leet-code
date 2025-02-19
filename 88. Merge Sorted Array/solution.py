from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Inicializa 'a' como o índice do último elemento válido em nums1
        a = m - 1
        # Inicializa 'b' como o índice do último elemento em nums2
        b = n - 1 
        # Inicializa 'c' como o índice do último espaço em nums1 onde podemos escrever
        c = m + n - 1 
        
        # Enquanto ainda houver elementos em nums2 a serem considerados
        while b >= 0:
            # Verifica se ainda há elementos válidos em nums1 e se o elemento atual de nums1 é maior que o de nums2
            if a >= 0 and nums1[a] > nums2[b]:
                # Se for verdade, copia o elemento de nums1 para a posição de escrita
                nums1[c] = nums1[a]
                # Move para o próximo elemento em nums1
                a -= 1
            else:
                # Caso contrário, copia o elemento de nums2 para a posição de escrita
                nums1[c] = nums2[b]
                # Move para o próximo elemento em nums2
                b -= 1
            
            # Move o índice de escrita para a esquerda, para a próxima posição disponível
            c -= 1