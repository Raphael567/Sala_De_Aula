def exibirMenuPrincipal() -> str:
    escolha = input("""
=================================
|         MENU PRINCIPAL        |
=================================
| [1] CADASTRAR ALUNO           |
| [2] EDITAR ALUNO              |
| [3] LISTAR ALUNOS             |
| [4] EXCLUIR ALUNOS            |
| [5] CALCULAR A MÉDIA DA SALA  |
| [6] CONSULTAR ALUNO           |
| [7] APAGAR SALA               |
| [8] INFORMAÇÔES               |
| [0] ENCERRAR                  |
=================================

SELECIONE UMA OPÇÃO: """)

    return escolha

def exibirMenuInformativo():
    escolha = input("""
=================================
|        MENU INFORMATIVO       |
=================================
| [1] CADASTRAR ALUNO           |
| [2] EDITAR ALUNO              |
| [3] LISTAR ALUNOS             |
| [4] EXCLUIR ALUNOS            |
| [5] CALCULAR A MÉDIA DA SALA  |
| [6] CONSULTAR ALUNO           |
| [7] APAGAR SALA               |
| [8] VOLTAR AO MENU ANTERIOR   | 
| [0] ENCERRAR                  |
=================================

SELECIONE UMA OPÇÃO: """)

    return escolha

def apresentaCadastrarAluno():
    print("""
==================================
|       [1] CADASTRAR ALUNO      |
|--------------------------------|
| Permite o cadastro de um novo  |
| aluno. Se o nome já existir, o |
| usuário pode optar por         |
| sobrepor as informações.       |
==================================
""")

def secaoCadastrarAluno():
    print("""
=================================
|      [1] CADASTRAR ALUNO      |
=================================
""")

def apresentaEditarAluno():
    print("""
==================================
|       [2] EDITAR ALUNO         |
|--------------------------------|
| Edita o nome e/ou a nota de um |
| aluno já registrado. Se o nome |
| for alterado, as notas são     |
| mantidas.                      |
==================================
""")

def secaoEditarAluno():
    print("""
=================================
|       [2] EDITAR ALUNO        |
=================================
""")

def apresentaListarAlunos():
    print("""
==================================
|       [3] LISTAR ALUNOS        |
|--------------------------------|
| Exibe todos os alunos          |
| registrados e suas respectivas |
| notas.                         |
==================================
""")

def secaoListarAlunos():
    print("""
=================================
|       [3] LISTAR ALUNOS       |
=================================
""")

def apresentaExcluirAlunos():
    print("""
==================================
|       [4] EXCLUIR ALUNOS       |
|--------------------------------|
| Remove um aluno do sistema.    |
| O sistema pergunta se o usuário|
| deseja realmente excluir o     |
| aluno selecionado.             |
==================================
""")

def secaoExcluirAlunos():
    print("""
=================================
|       [4] EXCLUIR ALUNOS      |
=================================
""")

def apresentaCalcularMediaSala():
    print("""
==================================
|   [5] CALCULAR A MÉDIA DA SALA |
|--------------------------------|
| Calcula e exibe a média das    |
| notas de todos os alunos       |
| cadastrados na sala.           |
==================================
""")

def secaoCalcularMediaSala():
    print("""
=================================
|   [5] CALCULAR A MÉDIA DA SALA|
=================================
""")

def apresentaConsultarAluno():
    print("""
==================================
|       [6] CONSULTAR ALUNO      |
|--------------------------------|
| Exibe a nota de um aluno       |
| específico. Se o aluno não     |
| estiver cadastrado, o sistema  |
| oferece a opção de cadastrá-lo.|
==================================
""")

def secaoConsultarAluno():
    print("""
=================================
|       [6] CONSULTAR ALUNO     |
=================================
""")

def apresentaApagarSala():
    print("""
==================================
|       [7] APAGAR SALA          |
|--------------------------------|
| Remove todos os alunos e       |
| notas da sala, esvaziando o    |
| sistema.                       |
==================================
""")

def secaoApagarSala():
    print("""
=================================
|       [7] APAGAR SALA         |
=================================
""")

def apresentaTrocaDeMenu():
    print("""
==================================
|        [8] TROCAR MENU         |
==================================
""")

def apresentaEncerrar():
    print("""
==================================
|         [0] ENCERRADO          |
==================================
""")
