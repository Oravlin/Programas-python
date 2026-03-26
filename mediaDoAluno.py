notas = []
media = 0
for x in range(0,3):
    notas.append(float(input(f"Insira a {x + 1}º nota do aluno:\n")))
    media =+ notas[x]
media /= 3

if media >= 8:
    conceito = 'A'
elif media >= 5 <= 8:
    conceito = 'B'
elif media <5:
    conceito = 'C'
    
print(f"A média do aluno foi de: {round(media)}\nE seu conceito foi de {conceito}")