import numpy as np
import pygame

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

PLAYER =0
AI = 1


class Plateau :

    def __init__(self):
        self.state = np.zeros((6,7))
        self.game_over = False
        self.turn = 0
        self.turn_mod=0

    def is_valid_move(self, col):
        return self.state[0, col] ==0

    def ligne_dispo(self, col):
        for ligne in range(5, -1, -1):
            if self.state[ligne, col]==0:
                return ligne


    def drop_piece(self, ligne, col, piece):
        self.state[ligne, col]=piece

    def print_board(self):
        print(self.state)

    def check_horizontal(self, piece):
        for ligne in range(6):
            for col in range(4):
                if self.state[ligne, col]==piece and self.state[ligne, col+1]==piece and self.state[ligne, col+2]==piece and self.state[ligne, col+3]==piece:
                    return True
        return False

    def check_vertical(self, piece):
        for ligne in range(3):
            for col in range(6):
                if self.state[ligne, col]==piece and self.state[ligne+1, col]==piece and self.state[ligne+2, col]==piece and self.state[ligne+3, col]==piece:
                    return True
        return False

    def check_diag(self, piece):
        for ligne in range(6):
            for col in range(7):
                col_1 =col +1
                ligne_1 = ligne + 1
                col_2 = col +2
                ligne_2 = ligne +2
                col_3 = col +3
                ligne_3 = ligne +3
                ligne_m1 = ligne - 1
                ligne_m2= ligne -2
                ligne_m3 = ligne -3

                #orientation \
                if self.state[ligne, col]==piece:
                    if ligne_1 <6 and col_1<7 and self.state[ligne_1, col_1] == piece:
                        if ligne_2 < 6 and col_2 < 7 and self.state[ligne_2, col_2] == piece:
                            if ligne_3 < 6 and col_3 < 7 and self.state[ligne_3, col_3] == piece:
                                return True
                #orientation /
                if self.state[ligne,col]==piece:
                    if ligne_m1>-1 and col_1<7 and self.state[ligne_m1, col_1] == piece:
                        if ligne_m2 > -1 and col_2 < 7 and self.state[ligne_m2, col_2] == piece:
                            if ligne_m3 > -1 and col_3 < 7 and self.state[ligne_m3, col_3] == piece:
                                return True
        return False


    def check_win(self, piece):
        return self.check_horizontal(piece) or self.check_vertical(piece) or self.check_diag(piece)


    def draw_board(self, screen, squaresize, radius):

        for col in range(7):
            for l in range(6):
                pygame.draw.rect(screen, BLUE, (col*squaresize, l*squaresize + squaresize, squaresize, squaresize))
                if self.state[l][col]==0:
                    pygame.draw.circle(screen, BLACK, (int(col*squaresize+squaresize/2), int(l*squaresize + squaresize + squaresize/2)), radius)
                elif self.state[l][col]==1:
                    pygame.draw.circle(screen, RED, (int(col * squaresize + squaresize / 2), int(l * squaresize + squaresize + squaresize / 2)), radius)
                elif self.state[l][col]==2:
                    pygame.draw.circle(screen, YELLOW, (int(col * squaresize + squaresize / 2), int(l * squaresize + squaresize + squaresize / 2)), radius)
        pygame.display.update()
