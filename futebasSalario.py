nome = input("Insira o seu nome:\n")
salario = float(input("Insira o salário atual do jogador:\n"))
aumento = 1.05

if salario <= 1000:
    aumento = 1.2
elif salario <= 5000:
    aumento = 1.1
    
print(f"Nome do jogador:\n{nome}\nO novo salário:\n{salario*aumento}")