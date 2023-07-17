valor = [0] * 5
listNumeros = []
inpar = []
par = []

quantidadeConsoantes = 0

for j in range(20):
    numero = int(input("Informe um número: "))
    listNumeros.append(numero)

for numero in listNumeros:
    if numero % 2 == 0:
        par.append(numero)
    else:
        inpar.append(numero)

print("Ímpar:", inpar)
print("Par:", par)
print("numeros listrados:", listNumeros)