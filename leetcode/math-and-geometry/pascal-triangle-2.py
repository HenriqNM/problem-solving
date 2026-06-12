class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        lista = [[1]]
        if rowIndex == 0:
            return lista[0]
        for n in range(0,rowIndex):
            lista.append([1,1])
            for i in range(len(lista[n])-1):
                resultado = lista[n][i]+lista[n][i+1]
                lista[n+1].insert(-1,resultado)
        return lista[rowIndex]