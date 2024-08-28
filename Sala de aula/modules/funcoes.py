from . import systems

def verificaNota(n: float) -> float:
    """ Verifica se a nota está entre 0 e 10 """
    if n < 0 or n > 10:
        raise ValueError("\nNOTA INVÁLIDA, DIGITE APENAS NÚMEROS ENTRE 0 E 10")
    return n

def ehFloat(n: str) -> float:
    """ Verifica se a string pode ser convertida para float e se a nota é válida """
    while True:
        try:
            n = float(n)
            n = verificaNota(n)
            return n
        except ValueError as e:
            if "could not convert string to float" in str(e):
                print("NOTA INVÁLIDA, DIGITE APENAS NÚMEROS ENTRE 0 E 10")
            else:
                print(e)

        n = input("DIGITE UMA NOTA VÁLIDA ENTRE 0 E 10: ")

def cadastraNota(d: dict, nome_aluno: str) -> None:
    """ Realiza o cadastro da nota """
    while True:
        try:
            nt_aluno = input("\nDIGITE UMA NOTA ENTRE 0 E 10: ")
            nt_aluno = ehFloat(nt_aluno)
            d[nome_aluno] = nt_aluno
            print(f"\nALUNO {nome_aluno} ADICIONADO COM SUCESSO!")
            break
        except ValueError:
            print("\nNOTA INVÁLIDA, DIGITE APENAS NÚMEROS ENTRE 0 E 10")

def verificaTexto(txt: str, prompt: str = None) -> str:
    """ Verifica se o valor passado é um texto válido """
    while not txt.isalpha() and not txt.replace(' ', '').isalpha():
        txt = input(prompt)
    return txt

def formataNome(nome_aluno: str) -> str:
    """ Realiza a padronização de escrita do nome (primeira letra maiúscula) """
    palavras = nome_aluno.split()
    palavra_formatada = []
    for palavra in palavras:
        palavra_formatada.append(palavra[0].upper() + palavra[1:].lower())
    nome_formatado = ' '.join(palavra_formatada)
    return nome_formatado

def inputNomeAluno(prompt: str) -> str:
    """ Entrada de dados do nome do aluno, com verificação e formatação """
    nm_aluno = input(prompt)
    nm_aluno = verificaTexto(nm_aluno, "\nNOME INVÁLIDO, DIGITE NOVAMENTE: ")
    nm_aluno = formataNome(nm_aluno)

    return nm_aluno

def atualizaChave(d: dict, chave_antiga: str, nova_chave: str) -> None:
    """ Atualiza o nome da key no dicionário """
    if chave_antiga in d:
        d[nova_chave] = d.pop(chave_antiga)
    else:
        print(f"CHAVE '{chave_antiga}' NÃO ENCONTRADA NO DICIONÁRIO")

def verificaIntencao(d: dict = None, func1=None, func2=None) -> bool:
    if func1 and func2:
        prompt = "DIGITE (C) PARA CADASTRAR, (S) PARA TENTAR NOVAMENTE OU (N) PARA ENCERRAR A AÇÃO: "
        opcoes_validas = ['C', 'S', 'N']
    else:
        prompt = "DIGITE (S) PARA CONTINUAR OU (N) PARA SAIR: "
        opcoes_validas = ['S', 'N']

    while True:
        intencao = input(prompt).upper()
        if intencao in opcoes_validas:
            break
        else:
            print(f"\nOPÇÃO INVÁLIDA! DIGITE NOVAMENTE {', '.join(opcoes_validas)}.")

    if intencao == 'C' and func1:
        func1(d)
    elif intencao == 'S' and func2:
        func2(d)
    elif intencao == 'N':
        print("\nAÇÃO ENCERRADA")

    return intencao == 'S'

def verificaDicionarioVazio(d: dict, acao_se_nao_vazio, acao_se_vazio) -> None:
    """ Verifica se o dicionário está vazio e executa ações correspondentes """
    if d:
        acao_se_nao_vazio()
    else:
        acao_se_vazio()

def verificaNomeExistente(d: dict, nm_aluno: str) -> bool:
    intencao = False
    if nm_aluno in d.keys():
        print("\nNOME JÁ EXISTENTE, DESEJA SOBREPOR?")
        intencao = verificaIntencao()
    else:
        cadastraNota(d, nm_aluno)

    return intencao

def cadastraAluno(d: dict) -> None:
    """ 1 - Cadastra o aluno e a sua nota """
    nm_aluno = inputNomeAluno("DIGITE O NOME DO ALUNO: ")

    if nm_aluno in d.keys():
        print("\nNOME JÁ EXISTENTE, DESEJA SOBREPOR?")
        intencao = verificaIntencao()

        if intencao:
            cadastraNota(d, nm_aluno)
    else:
        cadastraNota(d, nm_aluno)

def editarAluno(d: dict) -> None:
    """ 2 - Edita o aluno """
    def acao_se_nao_vazio():
        listarAlunos(d)

        nm_aluno = inputNomeAluno(" DIGITE O NOME DO ALUNO QUE DESEJA EDITAR: ")

        if nm_aluno in d:
            print("\nDESEJA MUDAR O NOME DO ALUNO?")
            intencao = verificaIntencao()

            if intencao:
                novo_nome = inputNomeAluno("\nDIGITE O NOVO NOME DO ALUNO: ")
                atualizaChave(d, nm_aluno, novo_nome)
                cadastraNota(d, novo_nome)
            else:
                cadastraNota(d, nm_aluno)
        else:
            print(f"\nO ALUNO {nm_aluno} NÃO ESTÁ REGISTRADO, DESEJA CADASTRÁ-LO, TENTAR NOVAMENTE OU ENCERRAR A AÇÃO?")
            verificaIntencao(d, lambda dict: cadastraNota(dict, nm_aluno), editarAluno)

    def acao_se_vazio():
        print("NÃO HÁ ALUNOS REGISTRADOS PARA EDIÇÃO")

    verificaDicionarioVazio(d, acao_se_nao_vazio, acao_se_vazio)

def listarAlunos(d: dict) -> None:
    """ 3 - Lista os alunos """
    def acao_se_nao_vazio():
        num_tabs = 4
        print("\nALUNOS" + "\t" * num_tabs + "NOTAS")
        print("=" * 40)
        for nome, nota in d.items():
            print(f"{nome}" + "\t" * num_tabs + f"{nota}")
        print("=" * 40)

    def acao_se_vazio():
        print("\nNÃO HÁ ALUNOS REGISTRADOS PARA EXIBIÇÃO")

    verificaDicionarioVazio(d, acao_se_nao_vazio, acao_se_vazio)

def excluirAluno(d: dict) -> None:
    """ 4 - Exclui os alunos """
    def acao_se_nao_vazio():
        print("DESEJA REALMENTE EXCLUIR UM ALUNO?")
        intencao = verificaIntencao()

        if intencao:
            listarAlunos(d)
            nm_aluno = inputNomeAluno("DIGITE O NOME DO ALUNO QUE DESEJA EXCLUIR: ")

            if nm_aluno in d:
                del d[nm_aluno]
                print(f"\nO(A) ALUNO(A) {nm_aluno} FOI EXCLUÍDO COM SUCESSO")
            else:
                print(f"\nALUNO {nm_aluno} NÃO ENCONTRADO")
        else:
            print("\nAÇÃO INTERROMPIDA")

    def acao_se_vazio():
        print("NÃO HÁ ALUNOS REGISTRADOS PARA EXCLUIR")

    verificaDicionarioVazio(d, acao_se_nao_vazio, acao_se_vazio)

def calculaMediaSala(d: dict) -> None:
    """ 5 - Calcula a média da sala """
    def acao_se_nao_vazio():
        media_sala = sum(d.values())/len(d)
        print(f"MÉDIA DA SALA = {round(media_sala, 1)}")

    def acao_se_vazio():
        print("NENHUMA NOTA DISPONÍVEL PARA O CÁLCULO DA MÉDIA")

    verificaDicionarioVazio(d, acao_se_nao_vazio, acao_se_vazio)

def consultarAluno(d: dict) -> None:
    """ 6 - Consulta o aluno indicado """
    def acao_se_nao_vazio():
        listarAlunos(d)

        nm_aluno = inputNomeAluno("DIGITE O NOME DO ALUNO QUE DESEJA CONSULTAR: ")

        if nm_aluno in d:
            systems.lineSystem()
            num_tabs = 4
            print("\nALUNO" + "\t" * num_tabs + "NOTA")
            print("=" * 25)
            print(f"{nm_aluno}" + "\t" * num_tabs + f"{d[nm_aluno]}")
            print("=" * 25)
        else:
            print(f"\nO ALUNO {nm_aluno} NÃO ESTÁ REGISTRADO, DESEJA CADASTRÁ-LO, TENTAR NOVAMENTE OU ENCERRAR A AÇÃO?")
            verificaIntencao(d, lambda dict: cadastraNota(dict, nm_aluno), consultarAluno)

    def acao_se_vazio():
        print("NÃO HÁ NENHUM ALUNO REGISTRADO PARA CONSULTA")

    verificaDicionarioVazio(d, acao_se_nao_vazio, acao_se_vazio)

def apagarSala(d: dict) -> None:
    """ 7 - Deleta a sala """
    def acao_se_nao_vazio():
        print("VOCÊ REALMENTE DESEJA EXCLUIR A SALA?")
        intencao = verificaIntencao()

        if intencao:
            d.clear()
            print("\nSALA EXCLUÍDA COM SUCESSO")
        else:
            print("\nAÇÃO INTERROMPIDA")

    def acao_se_vazio():
        print("\nNÃO HÁ NENHUMA SALA REGISTRADA PARA EXCLUIR")

    verificaDicionarioVazio(d, acao_se_nao_vazio, acao_se_vazio)
