from modules import enunciados, funcoes, dicionario, systems

def executarAcao(acao_func1, acao_func2=None, *args):
    systems.lineSystem()
    acao_func1()
    acao_func2(*args)
    systems.pauseSystem()

def menuPrincipal(escolha: int) -> None:
    match escolha:
        case 1:
            executarAcao(enunciados.secaoCadastrarAluno, funcoes.cadastraAluno, dicionario.notas)
        case 2:
            executarAcao(enunciados.secaoEditarAluno, funcoes.editarAluno, dicionario.notas)
        case 3:
            executarAcao(enunciados.secaoListarAlunos, funcoes.listarAlunos, dicionario.notas)
        case 4:
            executarAcao(enunciados.secaoExcluirAlunos, funcoes.excluirAluno, dicionario.notas)
        case 5:
            executarAcao(enunciados.secaoCalcularMediaSala, funcoes.calculaMediaSala, dicionario.notas)
        case 6:
            executarAcao(enunciados.secaoConsultarAluno, funcoes.consultarAluno, dicionario.notas)
        case 7:
            executarAcao(enunciados.secaoApagarSala, funcoes.apagarSala, dicionario.notas)
        case 8:
            executarAcao(menuInformativo)
        case 0:
            systems.lineSystem()
            enunciados.apresentaEncerrar()
            exit()

def menuInformativo() -> None:
    while True:
        escolha = enunciados.exibirMenuInformativo()

        match escolha:
            case "1":
                executarAcao(enunciados.apresentaCadastrarAluno)
            case "2":
                executarAcao(enunciados.apresentaEditarAluno)
            case "3":
                executarAcao(enunciados.apresentaListarAlunos)
            case "4":
                executarAcao(enunciados.apresentaExcluirAlunos)
            case "5":
                executarAcao(enunciados.apresentaCalcularMediaSala)
            case "6":
                executarAcao(enunciados.apresentaConsultarAluno)
            case "7":
                executarAcao(enunciados.apresentaApagarSala)
            case "0":
                systems.lineSystem()
                return
            case _:
                systems.lineSystem()
                print("\nOPÇÃO INVÁLIDA! TENTE NOVAMENTE.")
                systems.pauseSystem()
