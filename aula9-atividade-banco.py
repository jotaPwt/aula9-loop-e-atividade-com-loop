# ATIVIDADE 1

# Crie um sistema de banco, com as seguintes operações:

# ** Utilize While ou loop **

# # SISTEMA De banco

# - Acesso a conta

lista_acesso = []

cad_acesso = input('Cadastere seu acesso no banco: ')
print('Cadatro concluido')

lista_acesso.append(cad_acesso)

for i in range(1, 4):
    acesso = input('Digite seu acesso: ')
    if acesso == cad_acesso:
        print('Bem vindo a sua conta')  
        extrato = 1000
        print(f'Seu extrato atual é {extrato}')
    # - Fazer um deposito
        print('======================')
        print('Qual ação voce gostaria de realizar:')

        print('''
        id 0 = fazer um saque: 
        id 1 = fazer um depósito
        ''')

        acao = int(input('Digite o ID da ação desejada: '))

        if acao == 0:
            saque = int(input('insira o valor que voce gostaria sacar >>'))
            if saque > 1000:
                print('Voce nao tem todo esse dinheiro')
                pass
            elif saque <= 1000:
                print('Saque concluido')
                break
            elif saque == 0:
                print('nao é possivel sacar 0 reais')
            else:
                print('Ação indisponivel')
        elif acao == 1:
            dep = int(input('insira o valor que voce gostaria de depositar >>'))
            print('Depósito concluido com sucesso')
            break
        

    else:
        print(f'esse não é seu acesso. você tem {i} chances')
        if i > 2:
            print('Acesso Bloqueado')

# - Ver extrato
    
        
# - Fazer um saque 
# - Sair do sistema 


# ...........................................................

# ATIVIDADE 2

# CRIE A TABUADA COM O LOOP WHILE
# ESCOLHA UM NÚMERO E FAÇA O CALCULO DA MULTIPLICAÇÃO COM 
# TODOS OS NÚMEROS

