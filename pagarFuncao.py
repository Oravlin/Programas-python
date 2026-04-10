def totalPagar(valor, qtd):
    return valor * qtd
preco = float(input("Insira o valor unitário do produto:\n"))
quant = int(input("Insira a quantidade de produtos:\n"))
print(f"O total a pagar será de: R$: {round(totalPagar(preco, quant),2)}")