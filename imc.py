peso = float(input("Insira o seu peso:\n"))
altura = float(input("Insira a sua altura, em metros:\n"))

imc = peso/(altura*altura)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 24.9:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Acima do peso"
elif imc < 35:
    classificacao = "Obesidade classe I"
elif imc < 40:
    classificacao = "Obesidade classe II"
else:
    classificacao = "Obesidade classe III"
    
print(f"Seu IMC é de: {round(imc, 2)}\nSua classicação é {classificacao}")