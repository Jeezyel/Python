import random

vetorA = []
for i in range(10):
    vetorA.append(random.randint(1, 20))

soma = 0
for num in vetorA:
    soma += num ** 2

print('Vetor A: ', vetorA)
print('Soma dos quadrados: ', soma)