
idades = []
altura = []

for i in range(5):
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i+1)))
    altura = float(input('Digite a altura da {}ª pessoa: '.format(i+1)))
    idades.append(idade)
    altura.append(altura)

print('Idades na ordem inversa: ' )
for i in range(4, -1, -1):
    print(idades[i])

print('Alturas na ordem inversa: ')
for i in range(4, -1, -1):
    print(altura[i])

    