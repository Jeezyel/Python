def is_vowel(c):
    c = c.lower()
    return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'

vetor = []

print("Digite 10 caracteres:")

for _ in range(10):
    vetor.append(input())

contador_consoantes = 0
consoantes = []

for c in vetor:
    if c.isalpha() and not is_vowel(c):
        contador_consoantes += 1
        consoantes.append(c)

print("Quantidade de consoantes:", contador_consoantes)
print("Consoantes encontradas:", " ".join(consoantes))
