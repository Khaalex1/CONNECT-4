import numpy as np
from Board import *
import pygame
import sys
import math

# Fortement inspiré des vidéos de freeCampCode.org

if __name__ == '__main__':
    plateau = Plateau()
    print(plateau.state)

    pygame.init()

    SQUARESIZE = 100
    width = 7 * SQUARESIZE
    height = 7 * SQUARESIZE
    size = (width, height)
    RADIUS = int(SQUARESIZE / 2 - 5)

    screen = pygame.display.set_mode(size)
    plateau.draw_board(screen, SQUARESIZE, RADIUS)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)

    while True :

        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                posx = event.pos[0]
                if plateau.turn_mod == 0:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
                else :
                    pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                if plateau.turn_mod == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    #col = int(input("Au tour de Joueur 1 (0-6):"))

                    if plateau.is_valid_move(col):
                        ligne = plateau.ligne_dispo(col)
                        plateau.drop_piece(ligne, col, 1)

                        if plateau.check_win(1):
                            #print("JOUEUR 1 GAGNE")
                            label = myfont.render("Rouge gagne !", 1, RED)
                            screen.blit(label, (40, 10))
                            plateau.game_over = True
                else:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))
                    #col = int(input("Au tour de Joueur 2 (0-6):"))

                    if plateau.is_valid_move(col):
                        ligne = plateau.ligne_dispo(col)
                        plateau.drop_piece(ligne, col, 2)
                        if plateau.check_win(2):
                            #print("JOUEUR 2 GAGNE")
                            label = myfont.render("Jaune gagne !", 1, YELLOW)
                            screen.blit(label, (40, 10))
                            plateau.game_over = True

                # Nulle
                if plateau.turn == 41 and not plateau.game_over:
                    label = myfont.render("Match nul", 1, BLUE)
                    screen.blit(label, (40, 10))
                print(plateau.state)
                plateau.draw_board(screen, SQUARESIZE, RADIUS)

                plateau.turn += 1
                plateau.turn_mod = plateau.turn % 2

                if plateau.game_over:
                    pygame.time.wait(4000)



