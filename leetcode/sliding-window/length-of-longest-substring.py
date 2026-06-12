class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lista = []
        maior_tamanho = 0
        for letra in s:
            while letra in lista:
                lista.pop(0)
            lista.append(letra)
            if len(lista) > maior_tamanho:
                maior_tamanho = len(lista)
        return maior_tamanho