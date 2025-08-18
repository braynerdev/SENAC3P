from backends import criar_contato, listar_agenda_telefonica, editar_contato, remover_contato, excluir_todos
from models import agenda_telefonica

sair = 1

while sair == 1:
    try: 
        print("você deseja: \n1-Cadastrar Contato\n2-Listar Contatos\n3-Atualizar Contatos\n4-Excluir Contato\n5-Excluir Contatos")
        acao1 = int(input("Digíte o número da ação que você deseja executar: "))

        if acao1 < 1 or acao1 > 5:
            raise Exception("Só é permitido valor de 1 a 5!")
        
        if acao1 == 1:
            print("Preencha com alguns dados do seu contato!")

            nome = str(input("Nome: "))
            numeroTelefone = str(input("N° Telefone: "))
            email = str(input("Email: "))

            add_contato = criar_contato(nome,numeroTelefone,email)
            if add_contato:
                print("Contato adicionado com sucesso!")
            else:
                raise Exception(f"Não foi possivel adicionar {nome} a sua lista de contato!")
            
        elif acao1 == 2:
            listar_agenda_telefonica()
        
        elif acao1 == 3:
            listar_agenda_telefonica()
            idContato = str(input("Digíte o id do contato que você deseja editar: "))
            nome = str(input("Nome: "))
            numeroTelefone = str(input("NumeroTelefone: "))
            email = str(input("E-mail: "))
            editar_contato(idContato,nome,numeroTelefone,email)

        elif acao1 == 4:
            listar_agenda_telefonica()
            idContato = str(input("Digíte o id do contato que você deseja excluir: "))
            remover_contato(idContato)
        
        elif acao1 == 5:
            listar_agenda_telefonica()
            remover_contato()
            
        sair = int(input("Deseja sair? 1-Não 2-Sim: "))
        
    except ValueError:
        print("Valor inválido!")
        continue
    except Exception as e:
        print(e)
        continue