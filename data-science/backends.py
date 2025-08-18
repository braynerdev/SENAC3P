from models import agenda_telefonica
import uuid

def criar_contato(nome,numeroTelefone,email):
    dadosContato = {
                "id": str(uuid.uuid4())[:11],
                "nome": f"{nome}",
                "numeroTelefone": f"{numeroTelefone}",
                "email": f"{email}"
            }
    agenda_telefonica.append(dadosContato)
    return True


def listar_agenda_telefonica():
    if len(agenda_telefonica) > 0:
        for i, contato in enumerate(agenda_telefonica, start=1):
            print(f"contato {i} \nID: {contato['id']}\nNome: {contato['nome']}\nNúmero Telefone: {contato['numeroTelefone']}\nE-mail: {contato['email']}")
            print()
    else:
        raise Exception("Não existe nenhum contato salvo!")

def editar_contato(id,nome,numero,email):
    for i in agenda_telefonica:
        if i['id'] == id:
            i['nome'] = nome or i['nome']
            i['numeroTelefone'] = numero or i['numeroTelefone']
            i['email'] = email or i['email']
            print("conato editado!")
            return
    print("Contato não existe!")

def remover_contato(id):
    for i,contato in enumerate(agenda_telefonica,start=0):
        if contato['id'] == id:
            agenda_telefonica.pop(i)
            print("conato removido!")
            return
    print("Contato não existe!")

def excluir_todos():
    agenda_telefonica.clear()
    print("Conatatos removidos!")