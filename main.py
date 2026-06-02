from cramer import Cramer

tamanho = int(input("Qual a ordem da matriz?"))

matriz = []

for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        valor = float(input(f"Insira o elemento [{i}][{j}] da matriz: "))
        linha.append(valor)
    matriz.append(linha)

resultado = []
for i in range(tamanho):
    valor = float(input(f"Insira o resultado {i + 1}: "))
    resultado.append(valor)

lucro = []
for i in range(tamanho):
    valor = float(input(f"Insira o lucro {i + 1}: "))
    lucro.append(valor)

solucao = Cramer(matriz, resultado)

print(f"Soluções: {solucao.resolver()}")
print(f"Lucro: {solucao.lucro(lucro)}")