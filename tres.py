contador = 0
notas = 0

while contador < 4:
    print("Informe as notas:")
    notas += int(input())
    contador += 1

print(notas / 4)