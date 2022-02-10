from typing import List, Union

# Import and initialize the pygame library
import pygame
from pygame import Surface

from pygame.locals import (
    RLEACCEL,
    QUIT,
)

from piece_dict import piece_icons, my_pieces

pygame.init()

# The surface drawn on the screen is now an attribute of 'player'
class Piece(pygame.sprite.Sprite):
    def __init__(self, height: int, width: int, piece_type: str):
        super(Piece, self).__init__()
        self.is_selected = False
        self.row: int = 0
        self.col: int = 0 
        self.height: int = height
        self.width: int = width

        self.surf: Surface = pygame.image.load(piece_type).convert()
        self.surf = pygame.transform.scale(self.surf, (height, width))

        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    def get_row_and_col_offset(self, row: int, col: int):
        row_offset = row * self.height
        col_offset = col * self.width

        return row_offset, col_offset

    def update_cell_position(self, new_row: int, new_col: int):
        """Update the cell on which this piece is located"""
        row_offset = new_row * self.height
        col_offset = new_col * self.width

        self.rect.update(col_offset, row_offset, self.height, self.width)
        self.row = new_row
        self.col = new_col
    
    def derive_edges(self):
        """get rectangle list of rectangular cords representing edges of this pieces surface"""
        r1  = (0, 0, self.width, 1)
        r2 = (0, self.height -1, self.width, 1)
        r3 = (0, 0, 1, self.height)
        r4 = (self.width - 1, 0, 1, self.height)

        return [r1, r2, r3, r4]

    def select(self, screen: Surface):
        for r in self.derive_edges():
            self.surf.fill((255, 0, 0), r)

        screen.blit(self.surf, self.rect) #add to board


        self.is_selected = True
        print("selected piece")

    def de_select(self):
        pass

def get_piece_at_loc(row: int, col: int, pieces: List[Piece]) -> Union[Piece, None]:
    """takes a row and col and return the piece at specified location if it exists. Otherwise return None"""
    for piece in pieces:
        if row == piece.row and col == piece.col:
            return piece

    return None

def load_pieces(cell_size) -> List[Piece]:
    """Loads all the starting pieces at the start of the game. Returns a list all pieces (not ordered)"""
    piece_list = []
    for piece, loc in my_pieces["black"]["position"].items():
        for row, col in loc:
            new_piece = Piece(cell_size, cell_size, piece_icons[piece]) #create piece
            new_piece.update_cell_position(row, col) #initialize proper board location
            screen.blit(new_piece.surf, new_piece.rect) #add to board
            piece_list.append(new_piece)
    
    return piece_list

cellSize = 100
screen = Surface((cellSize * 8, cellSize * 8))

# Set up the drawing window
screen = pygame.display.set_mode([cellSize * 8, cellSize * 8,])

# Run until the user asks to quit
running = True

#This does not need to be here I Think. Prob bug once things start happening only need to generate board once,
#Only user event actions should occur here I think.
screen.fill((120, 255, 255))

for row in range(8):
    for col in range(8):
        if row % 2 == col % 2:
            pygame.draw.rect(screen, (255,255,255), (row*cellSize, col*cellSize, cellSize, cellSize))
        else:
            pygame.draw.rect(screen, (0,0,0), (row*cellSize, col*cellSize, cellSize, cellSize))
    
pieces = load_pieces(cellSize)

#Update the display
pygame.display.set_caption("ChessBoard")
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            col_pos, row_pos = pygame.mouse.get_pos()

            col = int(col_pos / cellSize)
            row = int(row_pos / cellSize)
            
            piece = get_piece_at_loc(row, col, pieces)

            if piece:
                piece.select(screen)

    pygame.display.flip()

#Done! Time to quit.
pygame.quit()
