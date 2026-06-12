class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        lista = [[1]]
        if numRows == 1:
            return lista
        for n in range(0,numRows-1):
            lista.append([1,1])
            for i in range(len(lista[n])-1):
                resultado = lista[n][i]+lista[n][i+1]
                lista[n+1].insert(-1,resultado)
        return lista