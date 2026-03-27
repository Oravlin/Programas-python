username = ["admin", "caio", "alvaro"]
senha = ["admin", "1234", "arroz-com-feijao"]

usernameInput = input("Insira o nome de usuário:\n")

tentativas = 0
while (tentativas < 3):
    if (usernameInput in username):
        userIndex = username.index(usernameInput)
        print("Usuário encontrado")
        senhaInput = input("Insira a senha:\n")
        if (senhaInput in senha and senha.index(senhaInput) == userIndex):
            print("Acesso concedido")
            break
        else:
            print("Acesso negado, tente novamente")
            tentativas += 1
    else:
        print("Usuário nâo encontrado, por favor tente novamente")
        tentativas += 1
        usernameInput = input("Insira o nome de usuário:\n")
if (tentativas > 2):
    print("Você gastou as três tentativas que tinha, acesso bloqueado")