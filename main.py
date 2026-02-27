
chamados = []

def criar_chamado():
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    
    chamado = {
        "titulo": titulo,
        "descricao": descricao,
        "status": "Aberto"
    }
    
    chamados.append(chamado)
    print("Chamado criado com sucesso!\n")


def listar_chamados():
    if not chamados:
        print("Nenhum chamado cadastrado.\n")
        return
    
    for i, c in enumerate(chamados):
        print(f"{i} - {c['titulo']} | {c['status']}")
    print()


def atualizar_status():
    listar_chamados()
    
    if not chamados:
        return
    
    try:
        indice = int(input("Digite o número do chamado: "))
        print("1 - Aberto")
        print("2 - Em andamento")
        print("3 - Resolvido")
        
        opcao = input("Novo status: ")
        
        if opcao == "1":
            chamados[indice]["status"] = "Aberto"
        elif opcao == "2":
            chamados[indice]["status"] = "Em andamento"
        elif opcao == "3":
            chamados[indice]["status"] = "Resolvido"
        else:
            print("Opção inválida.")
            return
        
        print("Status atualizado com sucesso!\n")
    
    except (ValueError, IndexError):
        print("Erro ao atualizar chamado.\n")


def excluir_chamado():
    listar_chamados()
    
    if not chamados:
        return
    
    try:
        indice = int(input("Digite o número do chamado para excluir: "))
        chamados.pop(indice)
        print("Chamado excluído com sucesso!\n")
    
    except (ValueError, IndexError):
        print("Erro ao excluir chamado.\n")


while True:
    print("===== SISTEMA DE CHAMADOS =====")
    print("1 - Criar chamado")
    print("2 - Listar chamados")
    print("3 - Atualizar status")
    print("4 - Excluir chamado")
    print("5 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        criar_chamado()
    elif opcao == "2":
        listar_chamados()
    elif opcao == "3":
        atualizar_status()
    elif opcao == "4":
        excluir_chamado()
    elif opcao == "5":
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida.\n")
