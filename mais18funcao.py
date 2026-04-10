def maior18(idade):
    if idade >= 18:
        return "O usuário é maior de idade."
    else:
        return "O usuário é menor de idade."

inputIdade = float(input("Insira a idade:\n"))

print(maior18(inputIdade))