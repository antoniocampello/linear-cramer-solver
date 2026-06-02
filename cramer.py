class Cramer:
    def __init__(self, matriz, resultados):
        self.matriz = matriz
        self.resultados = resultados

    def det2(self, m):
        return (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
    
    def det3(self, m):
        princiais = (
            m[0][0] * m[1][1] * m[2][2] +
            m[0][1] * m[1][2] * m[2][0] +
            m[0][2] * m[1][0] * m[2][1]
        )

        secundarias = (
            m[0][2] * m[1][1] * m[2][0] +
            m[0][0] * m[1][2] * m[2][1] +
            m[0][1] * m[1][0] * m[2][2]
        )

        return princiais - secundarias
    
    def escolherDet(self, m):
        if len(m) == 2:
            return self.det2(m)
        elif len(m) == 3:
            return self.det3(m)
        else:
            return None
    
    def trocar_coluna(self, coluna): # D, Dx ou Dy
        nova = []
        
        for i in range(len(self.matriz)):
            linha = self.matriz[i][:]
            linha[coluna] = self.resultados[i]

            nova.append(linha)
        
        return nova


    def resolver(self):
        R = self.escolherDet(self.matriz)

        if R == 0:
            return "Sistema sem solução"
        
        solucoes = []

        for col in range(len(self.matriz)):
            temp = self.trocar_coluna(col)
            detTrocada = self.escolherDet(temp)

            solucoes.append(detTrocada / R)
        
        return solucoes

    def lucro(self, lucros):
        solucoes = self.resolver()
        LT = 0

        for i in range (len(solucoes)):
            LT += solucoes[i] * lucros[i]

        return LT