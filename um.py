
vetor=[]

contador = 0

while contador < 5:
    vetor.append(input('informe um numero: ') )
    contador = contador + 1

while contador > 0:
    print(vetor.index(contador))
    contador = contador - 1



