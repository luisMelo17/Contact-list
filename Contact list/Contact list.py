def adicionar_contatos(contatos, nome_contato, telefone_contato, email_contato):
    contato = {"nome": nome_contato, "telefone": telefone_contato, "email": email_contato, "favorito": False}
    contatos.append(contato)
    print(f"O contato {nome_contato} foi adicionado na agenda.")
    return

def visualizar_contato(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        favorito = "(❤)" if contato["favorito"] else "( )"
        nome_contato = contato["nome"]
        print(f"{indice} {nome_contato} {favorito}")
    return

def editar_contatos(contatos, indice, propriedades):
    propriedades = int(propriedades)

    if propriedades == 1:
       novo_nome_contato = input("Qual vai ser o novo nome do contato: ")
    elif propriedades == 2:
        novo_numero_contato = int(input("Qual vai ser o novo numero do contato: "))
    elif propriedades == 3: 
        novo_email_contato = input("Qual vai ser o novo email do contato: ")
    else:
        print("Você digitou uma opção invalida")

    indice_corrigido = int(indice) - 1
    
    if propriedades == 1:
        contatos[indice_corrigido]["nome"] = novo_nome_contato
        print(f"Nome {novo_nome_contato} atualizado com sucesso")
    elif propriedades == 2:
        contatos[indice_corrigido]["telefone"] = novo_numero_contato
        print(f"Número {novo_numero_contato} atualizado com sucesso")
    elif propriedades == 3:
        contatos[indice_corrigido]["email"] = novo_email_contato
        print(f"Email {novo_email_contato} atualizado com sucesso")
    return

def favoritar_desfavoritar_contatos(contatos, estado):
    estado = int(estado)

    if estado == 1:
        a = "favoritar"
    elif estado == 2:
        a = "desfavoritar"
    else:
        print("Valor invalido")

    indice = int(input(f"Qual o numero do contato que você deseja {a}: "))
    indice_corrigido = indice - 1

    if estado == 1:
        contatos[indice_corrigido]["favorito"] = True
        print("Contato favoritado com sucesso.")
    elif estado == 2:
          contatos[indice_corrigido]["favorito"] = False
          print("Contato desfavoritado com sucesso.")
    return

def visualizar_contato_favorito(contatos):
    print("\nLista de contatos favoritos")
    for indice, contato in enumerate(contatos, start=1):
        favorito = contato["favorito"]
        nome_contato = contato["nome"]
        if favorito == True:
            favorito = "(❤)"
            print(f"{indice} {nome_contato} {favorito}")
    return

def apagar_contato(contatos, indice):
    indice_corrigido = int(indice) - 1
    contatos.pop(indice_corrigido)
    print(f"Contato {indice} removido com sucesso.")
    return 


contatos = []
while True:
    print("\nAgenda pessoal.")
    print("1. Adicionar um contato.")
    print("2. Visualisar contatos.")
    print("3. Editar contatos.")
    print("4. Favoritar e desfavoritar contatos.")
    print("5. Visualizar contatos favoritos.")
    print("6. Apagar um contato.")
    print("7. Sair do programa")

    try:
        escolha = int(input("Digite o numero da opção desejada: "))
        if escolha < 1 or escolha > 7:  # Verifica se a escolha está fora do intervalo válido
            print("Por favor, digite um número entre 1 e 7.")
            continue  # Volta ao início do loop para pedir uma nova entrada
    except ValueError:
        print("Por favor, digite um número válido.")
        continue  # Volta ao início do loop para pedir uma nova entrada

    if escolha == 1:
        try:
            nome_contato = input("\nQue nome deseja salvar nesse contato: ")
            if not nome_contato.isalpha():
                raise ValueError("O nome deve conter apenas letras!")

            telefone_contato = input("Insira o numero de telefone do contato: ")
            if not telefone_contato.isdigit():
                raise ValueError("O telefone deve conter apenas números!")
            
            email_contato = input("Insira o email do contato: ")
            if "@" not in email_contato or "." not in email_contato:
                raise ValueError("O email inserido não é valido!")
       
            adicionar_contatos(contatos, nome_contato, telefone_contato, email_contato)
        
        except ValueError as e:
            print(f"Houve um erro: {e}")

    elif escolha == 2:
        visualizar_contato(contatos)

    elif escolha == 3:
        visualizar_contato(contatos)
        try:
            indice = input("\nQual o numero do contato que você quer editar: ")
            if not indice.isdigit():
                raise ValueError("Houve um erro, digite um número valido!")

            print("Qual propriedade do contato você quer alterar: ")
            print("\n1. Nome.")
            print("2. Número.")
            print("3. Email.")

            propriedades = (input())
            if not propriedades.isdigit():
                raise ValueError("Houve um erro, digite um número valido!")

            editar_contatos(contatos, indice, propriedades)
        
        except ValueError as e:
            print(f"Houve um erro: {e}")

    elif escolha == 4:
        print("Selecione uma opção:")
        print("\n1. Favoritar contato")
        print("2. Desfavoritar contato")
        try:
            estado = input()
            if not estado.isdigit():
                raise ValueError("Houve um erro, digite apenas números!")
               
            visualizar_contato(contatos)
            favoritar_desfavoritar_contatos(contatos, estado)
        
        except ValueError as e:
            print(f"Houve um erro: {e}")

    elif escolha == 5: 
        visualizar_contato_favorito(contatos)

    elif escolha == 6:
        visualizar_contato(contatos)
        try:
            indice = input("Digite o número do contato que deseja excluir: ")
            if not indice.isdigit():
                raise ValueError("Houve um erro, digite apenas números!")

            apagar_contato(contatos, indice)

        except ValueError as e:
            print(f"Houve um erro: {e}")
       
    elif escolha == 7:
        break

print("Programa Finalizado.")