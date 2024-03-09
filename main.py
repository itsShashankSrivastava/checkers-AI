import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax

from alphaBeta.alphaBetaPrun import alphaBetaPruning

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

algo = "alphabeta"

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    
    alpha = float('inf')
    beta = float('-inf')
    
    while run:
        clock.tick(FPS)
        
        if game.turn == WHITE:
            if algo == "alphabeta":
                value, new_board = alphaBetaPruning(game.get_board(), 3, alpha, beta, WHITE, game, algo)
            
            else:
                value, new_board = minimax(game.get_board(), 3, WHITE, game, algo)
            game.ai_move(new_board)

        if game.winner(algo) != None:
            print(game.winner(algo))
            run = False

# Handles pygame events, such as quitting the game or selecting a square with the mouse.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    pygame.quit()

main()