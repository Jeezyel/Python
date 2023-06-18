
valor = [0] * 5  # Create a list of integers to store the values

contador = 0

while contador < 5:
    print("fale um numero")
    dados = int(input())
    valor[contador] = dados
    contador += 1
print("-----------------------")
while contador > 0:
    
    
    contador -= 1
    print(valor[contador])