vetor = []

contador = 0

while contador < 5:
    num = int(input("Digite um número inteiro: "))
    vetor.append(num)
    contador = contador + 1 

print("Vetor:", vetor)

soma = sum(vetor)
print("A soma dos números é:", soma)

mult = 1
for i in vetor:
    mult *= i
print("A multiplicação dos números é:", mult)