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
limite = 500    #LIMITE POR SAQUE
LIMITE_SAQUE = 3    #LIMITE DE SAQUES DIARIOS
extrato = ""
saques_efetuados = 0    #QUANTIDADE DE SAQUES JA EFETUADOS


while True:

    opcao = input(menu)  #DECISÃO DO CLIENTE A QUE MENU QUER ACESSAR


# DEPOSITO
    if opcao == "1":
        print("Você escolheu Depósito!")

        while True:

            deposito = int(input("Insira o Valor desejado: "))  #VALOR QUE O CLIENTE QUER DEPOSITAR
            
            #CASO O DEPOSITO NÃO SEJA VALOR POSITIVO

            if deposito <= 0:
                print("""
Erro!
Você deve depositar apenas valores positivos
""")
                
            
            #CASO O DEPOSITO SEJA COM VALOR POSITIVO

            elif deposito > 0:    
                print(f"Voce despositou R${deposito}")
                print("Retornando ao menu inicial!")
                saldo = (deposito + saldo)  #ATUALIZANDO O SALDO CONFORME O DEPOSITO
                extrato += f"Deposito: R$ {deposito:.2f}\n"  #ADICIONANDO O DEPOSITO NA LISTA PARA EXIBIR NO EXTRATO
                break
           
#SAQUE
    elif opcao == "2":
       
        print("Você escolheu Saque!")

        while True:
          
            sacar = int(input("Qual Valor deseja sacar? "))   #VALOR QUE O CLIENTE QUER SACAR
            
            #CASO LIMITE DE SAQUES DIARIOS NAO TENHA SIDO ULTRAPASSADO
            
            if saques_efetuados < LIMITE_SAQUE:
                
                #CASO SAQUE SEJA MAIOR QUE 0

                if sacar <= 0:      
                    print("Digite Um valor Valido!")
                    
                #CASO O SAQUE SEJA MENOR Q O LIMITE DE 500R$

                elif sacar <= limite:
               
                    #CASO SAQUE FOR MENOR Q O SALDO

                    if sacar <= saldo:
                        print("Saque realizado com sucesso!")
                        saldo = (saldo - sacar) #REDUZINDO DO SALDO 
                        print (f"Seu novo saldo é: {saldo}!")
                        print ("Retornando ao menu inicial!")
                        saques_efetuados = (saques_efetuados + 1)  #ATUALIZANDO QUANTIDADE DE SAQUES REALIZADOS NO DIA
                        extrato += (f'Saque: R${sacar:.2f}\n') #Adicionando o valor sacado a lista para exibir no extrato
                        break
                
                    #FALTA DE SALDO
            
                    else:
                        print("Não Foi possivel realizar o saque por falta de saldo!")

                # LIMITE DE 500R$ ULTRAPASSADO

                else:
                    print("Limite por saque Ultrapassado!")
            
            # LIMITE DE SAQUE DIARIO ATINGIDO
            
            elif saques_efetuados == LIMITE_SAQUE:
                print("Limite de saque diario atingido! Não é possivel realizar a operação!")
                break

#EXTRATO
    elif opcao == "3":
            
        print("Exibindo Extrato!")

        #EXTRATO COM AS INFORMÇÕES DE SAQUE E DEPOSITO

        print("\n========== EXTRATO ==========")
        print("Não Há movimentação!" if not extrato else extrato)
        print(f'\nSaldo Atual: R$ {saldo:.2f}')
        print("============= FIM =============")
  
    
    # OPÇÃO DE SAIR DO SISTEMA
    elif opcao == "4":
        print("Saindo! Obrigado por utilizar os nossos serviços!")
        break

    # NÃO DIGITOU DE 1 A 4
    else:
        print("Por Favor Escolha Uma Opção Valida!")
