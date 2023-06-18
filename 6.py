medias = []
contador_aprovados = 0

print('Digite as notas dos 10 alunos: ' )

# Lê as notas de cada aluno e calcula a média
for i in range(10):
    soma = 0

    for j in range(4):
        nota = float(input(f"Digite a nota {j+1} do aluno {i+1}: "))
        soma += nota

    media = soma / 4
    medias.append(media)

    if media >= 7.0:
        contador_aprovados += 1

print('Quantidade de alunos com média maior ou igual a 7.0: ', contador_aprovados)
