from modules import enunciados, systems
import menus

while True:

    escolha = enunciados.exibirMenuPrincipal()
    escolha = systems.isInt(escolha, 8)

    menus.menuPrincipal(escolha)
