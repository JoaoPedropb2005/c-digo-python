menu = """ 
    olá! Seja Bem Vindo(a) ao Nosso Sistema
             o que deseja fazer?
    (1) Depositar
    (2) Sacar
    (3) Extrato
    (0) Sair
"""

corrente = 2000.00
deposito = 0
opcao = 100
saque = 0
contador = 0
entrada = 0

while opcao != 0:
     
     print(menu)
     opcao = int(input( ))
     if opcao == 1:
        entrada = float(input("insira o valor do deposito: "))
        if entrada <= 0:
                print("valor não reconhecido.")
        elif entrada > 0:
                corrente += entrada
                deposito += entrada
                print("valor depositado!")
    
     if opcao == 2:
        entrada = float(input("insira o valor do saque: "))
        if contador > 3:
             print("limite de saque diário atingido")
        elif entrada > corrente:
             print("valor indisponível para saque")
        elif entrada <= 500.00:
             contador += 1
             corrente -= entrada
             saque += entrada
             print("saque efetuado!")
        elif entrada > 500:
             print("valor excede o limite máximo de saque.")
     
     if opcao == 3:
        if deposito or saque > 0:
            print(f"Extrato \nvalor total de depositos: {deposito}\nvalor total de saques: {saque}\nvalor atual disponível na conta: {corrente}")
        else:
            print("conta não sofreu movimentos!")

else: print("obrigado por usar nosso programa!!")
