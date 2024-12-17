class Solution:
    def conta_pares_reversos(self, vetor: list[int]):
        """
        Faz a contagem dos pares reversos a partir da divisão em L e R do vetor original, retornando cada parte ordenada, facilitando a contagem.
        """
        if len(vetor) <= 1:
            return vetor, 0
        
        metade = len(vetor) // 2
        lado_esq = vetor[:metade]
        lado_dir = vetor[metade:]
           
        # Separa o vetor em dois lados, L e R, já ordenados
        vetor_L, qtd_pares_L = self.conta_pares_reversos(lado_esq)
        vetor_R, qtd_pares_R = self.conta_pares_reversos(lado_dir)
        
        p_L = p_R = qtd_pares_reversos = 0
        vetor_ordenado = []
        
        # Conta os pares reversos de L e R
        j = 0
        for i in range(len(vetor_L)):
            while j < len(vetor_R) and vetor_L[i] > 2 * vetor_R[j]:
                j += 1
            qtd_pares_reversos += j
        
        # Ordena o vetor pela mesclagem
        while p_L < len(vetor_L) and p_R < len(vetor_R):
            if vetor_L[p_L] <= vetor_R[p_R]:
                vetor_ordenado.append(vetor_L[p_L])
                p_L += 1
            else:
                vetor_ordenado.append(vetor_R[p_R])
                p_R += 1
                
        # Termina de preencher o vetor
        while p_L < len(vetor_L):
            vetor_ordenado.append(vetor_L[p_L])
            p_L += 1

        while p_R < len(vetor_R):
            vetor_ordenado.append(vetor_R[p_R])
            p_R += 1

        # Retorne o vetor ordenado e a contagem total de pares reversos
        soma_pares_reversos = qtd_pares_L + qtd_pares_R + qtd_pares_reversos
        
        return vetor_ordenado, soma_pares_reversos

    def reversePairs(self, nums: list[int]) -> int:
        _, total_pairs = self.conta_pares_reversos(nums)

        return total_pairs