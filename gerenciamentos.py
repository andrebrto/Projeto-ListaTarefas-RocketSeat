def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa , "completada" : False}
    tarefas.append(tarefa)
    print(f"Tarefa [{nome_tarefa}] adicionada com sucesso")
    return

def ver_tarefas(tarefas):

    print("Lista de Tarefas")

    for indice, tarefa in enumerate(tarefas):
        status = "✔" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa} ")

def atualizar_tarefa(tarefas, indice_tarefa, nome_nova_tarefa):
    indice_tarefa_ajustado = indice_tarefa - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["tarefa"] = nome_nova_tarefa

        print(f"Tarefa {indice_tarefa} alterado para {nome_nova_tarefa}")
        
    else:
        print("indice informado é invalido")

def completar_tarefa(tarefas, indice_tarefa_completada):
    indice_tarefa_ajustado = indice_tarefa_completada - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["completada"] = True

        print(f"Tarefa {indice_tarefa_completada} completada com sucesso.")
    else:
        print("indice da tarefa informada é invalido")
    return
def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)
    
    print("Tarefas completadas removidas com sucesso!!")
tarefas = []



while True:
    print("\033[0;30;41mGerenciamento de tarefas\033[m")
    print("1. Adicionar Tarefa")
    print("2. Ver Tarefa")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar Tarefa Completada")
    print("6. Sair do Sistema")

    escolha = input("Digite sua opção: ")

    if escolha == "1":
        nome_tarefa = input("Digite sua tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    
    elif escolha == "2":
        ver_tarefas(tarefas)

    elif escolha == "3":
        ver_tarefas(tarefas)
        indice_tarefa = int(input("Digite o numero da tarefa: "))
        nome_nova_tarefa = input("Digite a nova Tarefa: ")
        atualizar_tarefa(tarefas, indice_tarefa, nome_nova_tarefa)
    elif escolha == "4":
        ver_tarefas(tarefas)
        indice_tarefa_completada = int(input("Digite a tarefa completada: "))
        completar_tarefa(tarefas, indice_tarefa_completada)
    elif escolha == "5":
        deletar_tarefas_completadas(tarefas)

    elif escolha == "6":
        print("\033[0;30;41mFinalizando Gerenciamento ...\033[m")
        break
