import os
from time import sleep
tarefas = []
def menu():
    print("-------- LISTA DE TAREFAS ---------")
    print("1 - Adicionar \n2 - Marcar tarefa como feita \n3 - Listar tarefas \n4 - Excluir uma tarefa \n5 - Limpar lista de tarefas\n")


def add(): tarefas.append(input("Insira o texto da tarefa: "))

def listar():
    os.system("cls")
    print("Tarefas")
    for i in range(len(tarefas)):
        print(i+1," ",tarefas[i])
def feita():
    listar()
    a=int(input("\nEscolha a posição da tarefa que deseja conluir: "))
    if a>=0 and a<=len(tarefas): tarefas[a-1]=tarefas[a-1]+"[OK]"

def remove():
    listar()
    a=int(input("\nEscolha a posição da tarefa que deseja excluir: "))
    if a>=0 and a<=len(tarefas): tarefas.pop(a-1)

def all():
    tarefas.clear()
    listar()
    print("\nLISTA LIMPADA COM SUCESSO")
    sleep(3)

while(True):
    os.system("cls")
    menu()
    op=int(input("Escolha a opção que deseja fazer: "))
    match op:
        case 1:
            add()
        case 2:
            feita()
        case 3:
            listar()
            sleep(2.5)
        case 4:
            remove()
        case 5:
            all()
        case _:
            break

