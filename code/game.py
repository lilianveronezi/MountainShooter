#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
from code.level import Level
from code.menu import Menu  # Importação corrigida

class Game:
    def __init__(self):
        pass

        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # Corrigido: agora usa self.window

    def run(self):
        while True:
            menu = Menu(self.window)  # Correção do nome da classe
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit() # Close WINDOW
                quit() #end paygame
            else:
                pass


