#Menu Inicial do Sistema

menu = ("""
        Por Favor Escolha Uma Opção:

            [1] - Depósito
            [2] - Saque
            [3] - Extrato
            [4] - Sair
""")

#Definindo Variaveis

saldo = 0
limite = 500
LIMITE_SAQUE = 3
extrato = ""
saques_efetuados = 0
d = list()
s = list()

while True:

    opcao = input(menu)


# DEPOSITO
    if opcao == "1":
        print("Você escolheu Depósito!")

        while True:
            deposito = int(input("Insira o Valor desejado: "))
            if deposito <= 0:
                print("""
Erro!
Você deve depositar apenas valores positivos
""")
                
            

            elif deposito > 0:    
                print(f"Voce despositou R${deposito}")
                print("Retornando ao menu inicial!")
                saldo = (deposito + saldo)
                d.append(deposito)
                break
           
#SAQUE
    elif opcao == "2":
       
        print("Você escolheu Saque!")

        while True:
          
            sacar = int(input("Qual Valor deseja sacar? "))
            
            if saques_efetuados < LIMITE_SAQUE:

                if sacar <= limite:
               
                    if sacar <= saldo:
                        print("Saque realizado com sucesso!")
                        saldo = (saldo - sacar)
                        print (f"Seu novo saldo é: {saldo}!")
                        print ("Retornando ao menu inicial!")
                        saques_efetuados = (saques_efetuados + 1)
                        s.append(sacar)
                        break
                
                    else:
                        print("Não Foi possivel realizar o saque por falta de saldo!")

                else:
                    print("Limite por saque Ultrapassado!")
            
            elif saques_efetuados == LIMITE_SAQUE:
                print("Limite de saque diario atingido! Não é possivel realizar a operação!")
                break

#EXTRATO
    elif opcao == "3":
            
        print("Exibindo Extrato!")

        print(f"""
            =========== EXTRATO ===========
           DEPOSITOS                  
           {d}    

           SAQUES
           {s}
            ===============================

""")      
    elif opcao == "4":
        print("Saindo! Obrigado por utilizar os nossos serviços!")
        break

    else:
        print("Por Favor Escolha Uma Opção Valida!")
