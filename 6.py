coluna = int(input())
operacao = input()

M = []
for _ in range(12):
    linha = []
    for _ in range(12):
        linha.append(float(input()))
    M.append(linha)

soma = 0
elementos = 0
for i in range(12):
    soma += M[i][coluna]
    elementos += 1

if operacao == 'S':
    print("{:.1f}".format(soma))
elif operacao == 'M':
    media = soma / elementos
    print("{:.1f}".format(media))
