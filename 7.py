def compare_strings(s1, s2):
    if len(s1) != len(s2):
        return len(s1) - len(s2)
    else:
        return 0

N = int(input())


casos_teste = []

for _ in range(N):
    strings = input().split()
    casos_teste.append(strings)

for strings in casos_teste:
    strings.sort(key=lambda x: (len(x), strings.index(x)))

for strings in casos_teste:
    print(*strings)
