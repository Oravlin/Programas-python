notas = []

while True:
    notaInput = float(input("Insira a nota do aluno, ou para cancelar, digite -1:\n"))
    
    if notaInput == -1:
        break
    else:
        notas.append(notaInput)

maiorNota = 0
menorNota = float("inf")
media = 0
    
for nota in notas:
    media += nota
    
    if nota > maiorNota:
        maiorNota = nota
    
    if nota < menorNota:
        menorNota = nota
     
media /= len(notas)
        
print(f"A média das notas inseridas é de: {round(media, 1)}\nA maior nota é: {maiorNota}\nA menor nota é: {menorNota}")