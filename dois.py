
valor = []  # Create a list of integers to store the values

contador = 0

while contador < 10:
    print("fale um numero")
    dados = int(input())
    valor.append(dados)  
    contador += 1
print("-----------------------")

for i in range(len(valor)-1, -1, -1):
    print(valor[i])
