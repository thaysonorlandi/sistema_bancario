import sys
import textwrap

def converte_real(valor):
    return "{:,.2f}".format(valor).replace(",", "X").replace(".", ",").replace("X", ".")


def verifica_saldo(valor):
    global saldo
    global contador_saque
    if valor > saldo:
        print("===================")
        print("Saldo indisponível!")
        print("===================")
    elif contador_saque > 2:
        print("==================================")
        print("Limite de saques diários excedido!")
        print("==================================")


def deposito(saldo, valor, historico_extrato):
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
    return saldo, historico_extrato


def extrato(saldo, /, *, historico_extrato):
    print("============ Extrato ================")
    print("Não foram realizadas movimentações." if not historico_extrato else historico_extrato)
    print("Seu saldo é de: R$", converte_real(saldo))
    print("=====================================")


def saque(*, saldo, valor, historico_extrato, contador_saque):
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
    return saldo, historico_extrato

def criar_usuario(usuarios):
    cpf = input("Informe seu cpf:")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário cadastrado com esse cpf!")
        return

    nome = input("Informe seu nome completo:")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa):")
    endereco = input("Informe seu endereço(logradouro, número, bairro, cidade, estado(sigla))")

    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco  })
    print("===== Usuário criado com sucesso!=====")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf ]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(AGENCIA, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("=== Conta criada com sucesso! ===")
        return {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado, fluxo de criação encerrado!")

def menu():
    menu = """\n
    ================ Menu ==============
    [1]\t Extrato;
    [2]\t Depósito;
    [3]\t Saque;
    [4]\t Nova Cliente;
    [5]\t Novo Conta;
    [9]\t Sair;
    """
    return int(input(textwrap.dedent(menu)))
            
def main():
    AGENCIA = "0001"
    
    saldo = 0
    contador_saque = 0
    valor = 0
    historico_extrato = ""
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        escolha = menu()

        if escolha == 1:
            extrato(saldo, historico_extrato=historico_extrato)

        elif escolha == 2:
            print("============================================================")
            valor = float(
                input("Digite qual o valor que você gostaria de depositar: R$ "))
            print("============================================================")
            saldo, historico_extrato = deposito(saldo, valor, historico_extrato)

        elif escolha == 3:
            print("============================================================")
            valor = float(input("Digite o valor que você gostaria de sacar: R$ "))
            print("============================================================")
            saldo, historico_extrato = saque(
                saldo=saldo,
                valor=valor,
                historico_extrato=historico_extrato,
                contador_saque=contador_saque)

        elif escolha == 5:
            conta = criar_conta(AGENCIA, numero_conta, usuarios) 

            if conta:
                contas.append(conta)
                numero_conta += 1
        
        elif escolha == 4:
            criar_usuario(usuarios)

        elif escolha == 9:
            sys.exit()

        else:
            print("===================================")
            print("Por favor digitar um valor válido!")
            print("===================================")
            sys.exit()

main()