
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

def listar_chamados():
    for i, c in enumerate(chamados):
        print(i, c["titulo"], "-", c["status"])
