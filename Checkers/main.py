import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED  
from checkers.board import Board
from checkers.game import Game

FPS = 60

# Sets the window for the game 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Displays Checkers in the corner 
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run =  True 
    
    # allows us to run the game on a certin fps 
    clock = pygame.time.Clock() 

    game = Game(WIN)

 
    while run :
        clock.tick(FPS)
        
        if game.winner() != None:
            print(game.winner())

        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                
                game.select(row, col)
             
        
        # draws the squares 
        game.update()

    # quits the game and closes the window 
    pygame.quit()
main()