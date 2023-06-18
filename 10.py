# Iniciando as variáveis contadoras e a lista de notas
notas = []
contador = 0

# Lendo notas até que o usuário digite um valor negativo
while True:
  nota = float(input("Digite uma nota (ou valor negativo para parar): "))
  if nota < 0:
    break 
  notas.append(nota)
  contador += 1

print("Quantidade de notas lidas: ", contador)
print("Notas digitadas: ", notas)
print("Notas digitadas na ordem inversa: ")
for nota in reversed(notas):
  print(nota)
soma_notas = sum(notas)
media_notas = soma_notas / contador
print("Soma das notas: ", soma_notas)
print("Média das notas: ", media_notas)
notas_acima_da_media = 0
for nota in notas:
  if nota > media_notas:
    notas_acima_da_media += 1
print("Quantidade de notas acima da média: ", notas_acima_da_media)
