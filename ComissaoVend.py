precoProd = float(input("Digite o valor da peça:\n"))
idVend = input("Digite a identificação do vendedor:\n")
codigoProd = input("Digite o código da peça:\n")
quantProd = int(input("Digite a quantidade da peças:\n"))
totalVenda = precoProd * quantProd
comissao = precoProd * 0.05
print("Identificação do vendedor: ", idVend, "\nCódigo da peça: ", codigoProd, "\nPreço unitário: ", precoProd, "\nQuantidade de peças: ", quantProd, "\nTotal da venda: ", totalVenda, "\nValor da comissão: ", comissao)