contagem_pares = 0
for _ in range(5):
    valor = int(input())
    if valor % 2 == 0:
        contagem_pares += 1

print("{} valores pares".format(contagem_pares))
