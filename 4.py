Ve = int(input())

N = [0] * 10
N[0] = Ve

for i in range(1, 10):
    N[i] = N[i - 1] * 2

for i in range(10):
    print("N[{}] = {}".format(i, N[i]))
