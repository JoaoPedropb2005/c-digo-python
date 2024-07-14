def menu ():
      global MENU
      print(MENU)

def op_deposito(valor):
    global entrada, corrente, depositos
    valor = entrada
    if entrada <= 0:
        print("Valor Não Aceito Para Depósito.")
    elif entrada > 0:
        corrente += entrada
        depositos += entrada
        print("Valor Depositado!")


def op_saque(valor):
     global contador, entrada, corrente, saques
     valor = entrada
     if contador >= 3:
             print("limite de saque diário atingido")
     elif entrada > corrente:
             print("valor indisponível para saque")    
     elif entrada <= 500.00:
             contador += 1
             corrente -= entrada
             saques += entrada
             print("saque efetuado!")
     elif entrada > 500:
             print("valor excede o limite máximo de saque.")

def op_extrato():
       global depositos, saques
       if depositos or saques > 0:
            print(f"Extrato \nvalor total de depositos: {depositos}\nvalor total de saques: {saques}\nvalor atual disponível na conta: {corrente}")
       else:
            print("conta não sofreu movimentos!")

"""def usuarios (nome, data, cpf, endereco):
    global cont_contas, copy
    cadastro = { }
    cadastro.fromkeys (["Nome", "Data de Nascimento", "Cpf", "Endereço"])
    cadastro.update({"Nome": nome, "Data de Nascimento": data, "Cpf": cpf, "Endereço": endereco})
    cadastro.update
    cont_contas += 1
    copy = cadastro.copy()"""

def usuarios (nome, data, cpf, endereco):
    global cont_contas, copy
    chaves = ["Nome", "Data de Nascimento", "cpf", "Endereço"]
    valores = [nome, data, cpf, endereco]
    lista = list(zip(chaves, valores))
    cadastros = dict(lista)
    print(cadastros)


def ver_contas ():
      global usuarios
      if cont_contas > 0:
          print(copy)
      else: print("não há contas registradas nesta sessão, crie uma para que seja exibida.")
      
      
MENU = """
 olá! Seja Bem Vindo(a) ao Nosso Sistema
             o que deseja fazer?
    (1) Depositar
    (2) Sacar
    (3) Extrato
    (4) Criar conta
    (5) Ver Contas
    (6) Sair do Sistema
"""
entrada = 0
corrente = 2000
depositos = 0
saques = 0
contador = 0 
opcao = 999
contas = 0
cont_contas = 0
copy = 0

"""VARIAVEIS /
entrada: (variavel que contabiliza os valores que o usuario entra nas operações de saque e deposito)
corrente: (variavel responsável por sofrer atribuições das entradas de saques, e decrementos das entradas de deposito)
depositos: (variavel que soma os depositos feitos dentro de uma sessão, para exibir seu valor no extrato)
saques: (variavel que soma os saques feitos pelo usuário, e a fim de mostrar o total de saques no extrato)
contador: (variavel de controle, que limita o numero de saques diários a 3)
opcao: (variavel que serve de mapeador do usuario no menu de funções do sistema)"""


while opcao != 0:

     menu()
     opcao = int(input( ))
     if opcao == 1:
          entrada = float(input("insira o valor do deposito: "))
          op_deposito(entrada)
     if opcao == 2:
          entrada = float(input("insira o valor do saque: "))
          op_saque(entrada)
     if opcao == 3:
          op_extrato()
     if opcao == 4:
           nome = input("Insira Seu Nome Completo: " )
           data = input("Insira Sua Data de Nascimento (DD/MM/AAAA): ")
           cpf = input("Insira Seu CPF (Apenas Números): ")
           endereco = input("Insira seu Endereço (Estado, Cidade, Bairro): ")
           usuarios(nome, data, cpf, endereco)
     if opcao == 5:
           ver_contas()
else: print("obrigado por usar nosso programa!!") 