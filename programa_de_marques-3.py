#Matheus Marques de Melo Silva

import time


lista = []
nomes = []
endereços = []
telefones = []

pessoal_nome = []
pessoal_endereço = []
pessoal_telefone = []

profissional_nome = []
profissional_endereço = []
profissional_telefone = []

romântico_nome = []
romântico_endereço = []
romântico_telefone = []


print("Olá meu caro usuário, aqui é seu aplicativo de agenda dos seus contatos, ok?")
time.sleep(0)
print("Você vai inserir algumas informações aqui.")
time.sleep(0)
print("Sempre lembre de salvar sua lista, se não salvar, você não obterá os dados.")

def tela_inicial():
    print(""" 
          -------------------------------
                 AGENDA TELEFÔNICA
          -------------------------------\n
    Pressione 'c' para criar um contato.\n
    Pressione 'e' para editar o contato.\n
    Pressione 'x' para excluir o contato.\n
    Pressione 'l' para listar os contatos.(Serão exibidos os contatos listados)\n
    Pressione 's' para salvar a sua lista.(Todos os contatos serão exibidos em um arquivo .txt)""")
    botão_user = input("Digite aqui: ")
    botão_user = botão_user.strip()
    botão_user = botão_user.upper()
    if botão_user == "C":
        criar()
    elif botão_user == "S":
        save()
    elif botão_user == "L":
        listar()
    elif botão_user == "X":
        excluir()
    elif botão_user == "E":
        editar()
    else:
        print("Selecione um valor válido.")
        time.sleep(1)
        tela_inicial()

    
def criar():
    nome = input("Insira o nome do contato: ")
    if nome == "":
        nome = "Não definido"
    nomes.append(nome)
    
    endereço = input("Insira o endereço: ")
    if endereço == "":
        endereço = "Não definido"
    endereços.append(endereço)
    
    telefone = input("Insira o telefone: ")
    if telefone == "":
        telefone = "Não definido"
    telefones.append(telefone)

    #SISTEMA DE LISTAGEM

    Controlador = False
    Controlador2 = False

    while Controlador == False:
        listagem = input("Você deseja listar o contato? y/n")
        if listagem == "y" or listagem == "Y":
            while Controlador2 == False:
                escolha_listagem = input("""
Pressione 1 para pessoal
Pressione 2 para profissional
Pressione 3 para romântico.
Insira: """)
                if escolha_listagem == "1":
                    print("Você selecionou o seu contato como: 'Pessoal'")
                    Controlador2 = True
                    pessoal_nome.append(nome.strip())
                    pessoal_endereço.append(endereço.strip())
                    pessoal_telefone.append(telefone.strip())
                    Controlador = True
                elif escolha_listagem == "2":
                    print("Você selecionou o seu contato como: 'Profissional'")
                    Controlador2 = True
                    profissional_nome.append(nome.strip())
                    profissional_endereço.append(endereço.strip())
                    profissional_telefone.append(telefone.strip())
                    Controlador = True
                elif escolha_listagem == "3":
                    print("Você selecionou o seu contato como: 'Romântico'")
                    Controlador2 = True
                    romântico_nome.append(nome)
                    romântico_endereço.append(endereço)
                    romântico_telefone.append(telefone)
                    Controlador = True
                else:
                    print("Escolha um número válido.")
        elif listagem == "n" or listagem == "N":
            print("Tudo bem, não vamos listar esse contato.")
            time.sleep(1)
            Controlador = True
        else:
            print("Por favor, selecione alguma opção.")
    
    controlador3 = False
    while controlador3 == False:
        confirma1 = input("Você deseja continuar adicionando contatos? y/n")
        confirma1 = confirma1.strip()
        confirma1 = confirma1.upper()
        if confirma1 == "Y":
            criar()
            controlador3 = True
        elif confirma1 == "N":
            print("Ok, vamos voltar para a página inicial.")
            tela_inicial()
            controlador3 = True
        else:
            print("Selecione alguma resposta válida.")

def save():
    print("Sua agenda foi salva.\nOlhe o arquivo 'Agenda.txt'")
    agenda = open("Agenda.txt", encoding = "utf-8", mode= "w")
    for nome, endereço, telefone in zip(nomes, endereços, telefones):
        nome = nome.strip()
        endereço = endereço.strip()
        telefone = telefone.strip()
        agenda.write(f"{nome}, {endereço}, {telefone}\n")
    
    time.sleep(1)
    agenda.close()
    tela_inicial()

def listar():
    print("Você verá apenas os seus contatos listados.\n")
    time.sleep(1)
    for nome1, endereço1, telefone1 in zip(pessoal_nome, pessoal_endereço, pessoal_telefone):
        print("Contatos pessoais:")
        print(f"{nome1}, {endereço1}, {telefone1}.\n")
    for nome2, endereço2, telefone2 in zip(profissional_nome, profissional_endereço, profissional_telefone):
        print("Contatos profissionais:")
        print(f"{nome2}, {endereço2}, {telefone2}.\n")
    for nome3, endereço3, telefone3 in zip(romântico_nome, romântico_endereço, romântico_telefone):
        print("Contatos profissionais:")
        print(f"{nome3}, {endereço3}, {telefone3}.\n")
    time.sleep(2)
    tela_inicial()
    
def excluir():
    time.sleep(1)
    print("""Para excluir você seleciona a posição do contato, com base na ordem que você criou a agenda.
1 - Primeiro contato.
2 - Segundo contato...""")
    resp_excluir =  int(input("Selecione qual contato que você deseja excluir: "))
    indice_exclusao = resp_excluir - 1
    if resp_excluir > len(nomes):
        print("Seu número excede a quantidade de contatos.")
    elif resp_excluir <= 0:
        print("Coloque um número válido.")
    else:
        for x in range(len(pessoal_telefone)):
            for telefone_pessoal in pessoal_telefone:
                if telefone_pessoal == telefones[indice_exclusao]:
                    del pessoal_nome[x]
        
        for y in range(len(profissional_telefone)):
            for telefone_profissional in profissional_telefone:
                if telefone_profissional == telefones[indice_exclusao]:
                    del profissional_nome[y]

        for z in range(len(romântico_telefone)):
            for telefone_romântico in romântico_telefone:
                if telefone_romântico == telefones[indice_exclusao]:
                    del romântico_nome[z]

        del nomes[indice_exclusao]
        del endereços[indice_exclusao]
        del telefones[indice_exclusao]
        print(f"O contato de posição '{resp_excluir}' foi excluído.")
    
    
    
    time.sleep(1)
    tela_inicial()

def editar():
    controlador = False
    time.sleep(1)
    print("""Para editar você seleciona a posição do contato, com base na ordem que você criou a agenda.
1 - Nome.
2 - Endereço
3 - Telefone""")
    while controlador == False:
        resp_user = input("Selecione o que você deseja editar: ")
        resp_user = resp_user.strip()
        if resp_user == "1":
            controlador = True
            nomes_1()
        elif resp_user == "2":
            controlador = True
            endereços_1()
        elif resp_user == "3":
            controlador = True
            telefones_1()
        else:
            print("Escreva um número válido.")
            
def nomes_1():
    print("Você selecionou para editar o nome.")
    resp_user_1 = int(input("""Qual contato você deseja editar o nome?
1 - Primeiro contato que você criou na agenda.
2 - Segundo contato que você criou na agenda
(...)"""))
    indice_editor = resp_user_1 - 1
    if resp_user_1 > len(nomes):
            print("O número que você digitou excede a quantidade de contatos.")
    elif resp_user_1 <= 0:
            print("Por favor, selecione um número válido.")
    else:
        resp_user_novo_nome = input("Escreva o novo nome: ")
        
        for x in range(len(pessoal_telefone)):
            for telefone_pessoal in pessoal_telefone:
                if telefone_pessoal == telefones[indice_editor]:
                    pessoal_nome[x] = resp_user_novo_nome
        
        for y in range(len(profissional_telefone)):
            for telefone_profissional in profissional_telefone:
                if telefone_profissional == telefones[indice_editor]:
                    profissional_nome[y] = resp_user_novo_nome

        for z in range(len(romântico_telefone)):
            for telefone_romântico in romântico_telefone:
                if telefone_romântico == telefones[indice_editor]:
                    romântico_nome[z] = resp_user_novo_nome
        




        nomes[indice_editor]= resp_user_novo_nome
        
        print(f"O nome do seu contato agora é: {resp_user_novo_nome}")
        
    tela_inicial()
    
def endereços_1():
    print("Você selecionou para editar o endereço.")
    resp_user_1 = int(input("""Qual contato você deseja editar o endereço?
1 - Primeiro contato que você criou na agenda.
2 - Segundo contato que você criou na agenda
(...)"""))
    indice_editor = resp_user_1 - 1
    if resp_user_1 > len(nomes):
            print("O número que você digitou excede a quantidade de contatos.")
    elif resp_user_1 <= 0:
            print("Por favor, selecione um número válido.")
    else:
        resp_user_novo_nome = input("Escreva o novo endereço: ")
        
        for x in range(len(pessoal_telefone)):
            for telefone_pessoal in pessoal_telefone:
                if telefone_pessoal == telefones[indice_editor]:
                    pessoal_endereço[x] = resp_user_novo_nome
        
        for y in range(len(profissional_telefone)):
            for telefone_profissional in profissional_telefone:
                if telefone_profissional == telefones[indice_editor]:
                    profissional_endereço[y] = resp_user_novo_nome

        for z in range(len(romântico_telefone)):
            for telefone_romântico in romântico_telefone:
                if telefone_romântico == telefones[indice_editor]:
                    romântico_endereço[z] = resp_user_novo_nome
        




        endereços[indice_editor]= resp_user_novo_nome
        
        print(f"O endereço do seu contato agora é: {resp_user_novo_nome}")
        
    tela_inicial()

def telefones_1():
    print("Você selecionou para editar o telefone.")
    resp_user_1 = int(input("""Qual contato você deseja editar o telefone?
1 - Primeiro contato que você criou na agenda.
2 - Segundo contato que você criou na agenda
(...)"""))
    indice_editor = resp_user_1 - 1
    if resp_user_1 > len(nomes):
            print("O número que você digitou excede a quantidade de contatos.")
    elif resp_user_1 <= 0:
            print("Por favor, selecione um número válido.")
    else:
        resp_user_novo_nome = input("Escreva o novo telefone: ")
        
        for x in range(len(pessoal_telefone)):
            for telefone_pessoal in pessoal_telefone:
                if telefone_pessoal == telefones[indice_editor]:
                    pessoal_telefone[x] = resp_user_novo_nome
        
        for y in range(len(profissional_telefone)):
            for telefone_profissional in profissional_telefone:
                if telefone_profissional == telefones[indice_editor]:
                    profissional_telefone[y] = resp_user_novo_nome

        for z in range(len(romântico_telefone)):
            for telefone_romântico in romântico_telefone:
                if telefone_romântico == telefones[indice_editor]:
                    romântico_telefone[z] = resp_user_novo_nome
        




        telefones[indice_editor]= resp_user_novo_nome
        
        print(f"O telefone do seu contato agora é: {resp_user_novo_nome}")
        
    tela_inicial()


tela_inicial()
