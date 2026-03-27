nomes = []
idades = []
mais18 = 0
while True:
    print("DIGITE 'ENCERRAR' PARA CANCELAR")
    nomeInput = input("Insira o nome do usuário:\n")
    if nomeInput == "encerrar":
        break
    else:
        idadeInput = int(input("Insira a idade do usuário:\n"))
    nomes.append(nomeInput)
    idades.append(idadeInput)

for idade in idades:
    if idade >= 18:
        mais18 += 1

print(f"Total de usuários cadastrados: {len(nomes)}\nQuantidade de usuários maiores de 18 anos: {mais18}")