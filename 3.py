X, Y = map(int, input().split())

if X > Y:
    X, Y = Y, X

soma = 0


for num in range(X, Y + 1):
    if num % 13 != 0:
        soma += num

print(soma)
