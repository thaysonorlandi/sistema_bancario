import sys

saldo = 0
contador_saque = 0
valor = 0
historico_extrato = ''


def converte_real(valor):
    return "{:,.2f}".format(valor).replace(",", "X").replace(".", ",").replace("X", ".")


def verifica_saldo(valor):
    global saldo
    if valor > saldo:
        print("===================")
        print("Saldo indisponível!")
        print("===================")
    elif contador_saque > 2:
        print("==================================")
        print("Limite de saques diários excedido!")
        print("==================================")


def deposito(valor):
    global historico_extrato
    global saldo
    if valor > 0:
        saldo += valor
        historico_extrato += f"Depósito: R$ {converte_real(saldo)}\n"
        print("==============================================================")
        print("Valor depositado com sucesso! Seu saldo atual é de: R$",
              converte_real(saldo))
        print("==============================================================")
    else:
        print("==================================")
        print("Por favor insira um número válido!")
        print("==================================")


def extrato():
    global historico_extrato
    global saldo
    print("============ Extrato ================")
    print("Não foram realizadas movimentações." if not historico_extrato else historico_extrato)
    print("Seu saldo é de: R$", converte_real(saldo))
    print("=====================================")


def saque(valor):
    global historico_extrato
    global contador_saque
    global saldo
    if contador_saque < 3 and valor < saldo:
        if 0 < valor <= 500 and valor < saldo:
            saldo -= valor
            contador_saque += 1
            historico_extrato += f"Saque: R$ {converte_real(saldo)}\n"
            print(
                "=================================================================")
            print("Saque efetuado com sucesso! Seu saldo restante é de: R$",
                  converte_real(saldo))
            print(
                "=================================================================")
        else:
            print(
                "=====================================================================================================")
            print(
                "Valor de saque maior que o limite permitido por saque, o valor deve ser igual ou inferior a R$ 500,00")
            print(
                "=====================================================================================================")
    else:
        verifica_saldo(valor)


while True:
    print("Qual operação você deseja realizar?")
    print("1. Extrato;")
    print("2. Depósito;")
    print("3. Saque;")
    print("9. Sair.")

    escolha = int(input())

    if escolha == 1:
        extrato()
    elif escolha == 2:
        print("============================================================")
        valor = float(
            input("Digite qual o valor que você gostaria de depositar: R$ "))
        print("============================================================")
        deposito(valor)
    elif escolha == 3:
        print("============================================================")
        valor = float(input("Digite o valor que você gostaria de sacar: R$ "))
        print("============================================================")
        saque(valor)
    elif escolha == 9:
        sys.exit()
    else:
        print("===================================")
        print("Por favor digitar um valor válido!")
        print("===================================")
        sys.exit()
