from modules import enunciados, funcoes, dicionario, systems

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
            executarAcao2(enunciados.apresentaTrocaDeMenu)
            executarAcao2(menuInformativo)
        case 0:
            systems.lineSystem()
            enunciados.apresentaEncerrar()
            exit()

def menuInformativo() -> None:
    while True:
        escolha = enunciados.exibirMenuInformativo()

        match escolha:
            case "1":
                executarAcao2(enunciados.apresentaCadastrarAluno)
            case "2":
                executarAcao2(enunciados.apresentaEditarAluno)
            case "3":
                executarAcao2(enunciados.apresentaListarAlunos)
            case "4":
                executarAcao2(enunciados.apresentaExcluirAlunos)
            case "5":
                executarAcao2(enunciados.apresentaCalcularMediaSala)
            case "6":
                executarAcao2(enunciados.apresentaConsultarAluno)
            case "7":
                executarAcao2(enunciados.apresentaApagarSala)
            case "8":
                executarAcao2(enunciados.apresentaTrocaDeMenu)
                return
            case "0":
                systems.lineSystem()
                enunciados.apresentaEncerrar()
                exit()
            case _:
                systems.lineSystem()
                print("\nOPÇÃO INVÁLIDA! TENTE NOVAMENTE.")
                systems.pauseSystem()

def executarAcao(acao_func1, acao_func2=None, *args):
    systems.lineSystem()
    acao_func1()
    acao_func2(*args)
    systems.pauseSystem()

def executarAcao2(acao_func):
    systems.lineSystem()
    acao_func()
    systems.pauseSystem()