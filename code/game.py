#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.menu import Menu  # Importação corrigida

class Game:
    def __init__(self):
        pass

        pygame.init()
        self.window = pygame.display.set_mode((600, 480))  # Corrigido: agora usa self.window

    def run(self):
        while True:
            menu = Menu(self.window)  # Correção do nome da classe
            menu.run()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fecha a janela
                    quit()  # Encerra o pygame
