def systemOut():
    print("\nEncerrado...")
    exit()

def lineSystem() -> None:
    print("\n" * 100)

def pauseSystem() -> None:
    input("\nPRESSIONE ENTER PARA CONTINUAR...")
    lineSystem()

def choiceSystem() -> int:
    escolha = int(input("DIGITE UMA OPÇÃO: "))
    return escolha

def isInt(n: str, qtd_opt: int) -> int:
    while True:
        try:
            n = int(n)
            if n < 0 or n > qtd_opt:
                raise ValueError("\nOpção inválida, digite apenas os valores das opções")
            return n
        except ValueError:
            print("\nOpção inválida, digite apenas os valores das opções")

        n = input("Digite a sua escolha: ")
