from typing import List, Union

# Import and initialize the pygame library
import pygame
from pygame import Surface

from pygame.locals import (
    RLEACCEL,
    QUIT,
)

from piece_dict import piece_icons, my_pieces

    

# The surface drawn on the screen is now an attribute of 'player'
class Piece(pygame.sprite.Sprite):
    def __init__(self, height: int, width: int, piece_type: str, color: str):
        super(Piece, self).__init__()
        self.color = color
        self.piece_type = piece_type
        self.is_selected = False
        self.row: int = 0
        self.col: int = 0 
        self.height: int = height
        self.width: int = width

        self.surf: Surface = self.create_surface()
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
        """get list of rectangular cords representing edges of this pieces surface"""
        r1  = (0, 0, self.width, 1)
        r2 = (0, self.height -1, self.width, 1)
        r3 = (0, 0, 1, self.height)
        r4 = (self.width - 1, 0, 1, self.height)

        return [r1, r2, r3, r4]

    def select(self, screen: Surface):
        "highllight piece and set it's is_selected property to True"
        for r in self.derive_edges():
            self.surf.fill((255, 0, 0), r)

        screen.blit(self.surf, self.rect) #add to board
        self.is_selected = True
    
    def de_select(self, screen: Surface):
        for r in self.derive_edges():
            self.surf.fill((0, 0, 0), r)

        screen.blit(self.surf, self.rect) #add to board
        self.is_selected = False            

    def create_surface(self):
        surf = pygame.image.load(self.piece_type).convert()
        surf = pygame.transform.scale(surf, (self.height, self.width))
        surf.set_colorkey((255, 255, 255), RLEACCEL)

        return surf


class Board():

    def __init__(self, cell_size: int) -> None:
        self.cell_size = cell_size
        self.ROWS = 8
        self.COLS = 8
        self.selected_piece = None

        self.screen = self.set_up_screen(cell_size)
        self.draw_board(cell_size)
        self.load_pieces(cell_size)

    def set_up_screen(self, cell_size):
        """Create our screen object which we will be drawing on"""
        screen = Surface((cell_size * 8, cell_size * 8))

        # Set up the drawing window
        screen = pygame.display.set_mode([cell_size * 8, cell_size * 8])

        #Update the display
        pygame.display.set_caption("ChessBoard")

        return screen

    def draw_board(self, cell_size: int):
        """Draws alternating color chessboard with each tile being dims: cell_size by cell_size"""
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if row % 2 == col % 2:
                    pygame.draw.rect(self.screen, (255,255,255), (row*cell_size, col*cell_size, cell_size, cell_size))
                else:
                    pygame.draw.rect(self.screen, (0,0,0), (row*cell_size, col*cell_size, cell_size, cell_size))
    
    def load_color(self, cell_size: int, color: str) -> List[Piece]:
        """Loads all the starting pieces of specified color for start of the game. Returns a list all pieces (not ordered)"""
        piece_list = []
        for piece, loc in my_pieces[color]["position"].items():
            for row, col in loc:
                new_piece = Piece(cell_size, cell_size, piece_icons[color][piece], color) #create piece
                new_piece.update_cell_position(row, col) #initialize proper board location
                self.screen.blit(new_piece.surf, new_piece.rect) #add to board
                piece_list.append(new_piece)
        
        return piece_list
    
    def load_pieces(self, cell_size) -> List[Piece]:
        """Loads all the starting pieces for start of the game. Returns a list all pieces (not ordered)"""
        black_pieces = self.load_color(cell_size, color = "black")
        white_pieces = self.load_color(cell_size, color = "white")

        return black_pieces + white_pieces


    def handle_selection(self, piece: Piece):
        if self.selected_piece:
            self.selected_piece.de_select(self.screen)
            
        self.selected_piece = piece
        piece.select(self.screen)

def get_piece_at_loc(row: int, col: int, pieces: List[Piece]) -> Union[Piece, None]:
    """takes a row and col and return the piece at specified location if it exists. Otherwise return None"""
    for piece in pieces:
        if row == piece.row and col == piece.col:
            return piece

    return None

pygame.init()

cellSize = 100
new_board = Board(cellSize)

# Run until the user asks to quit
running = True

pieces = new_board.load_pieces(cellSize)

while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Get mouse click event
        if event.type == pygame.MOUSEBUTTONDOWN:
            col_pos, row_pos = pygame.mouse.get_pos()

            col = int(col_pos / cellSize)
            row = int(row_pos / cellSize)
            
            piece = get_piece_at_loc(row, col, pieces) #check if there is a piece at mouseclick location

            if piece:
                new_board.handle_selection(piece)

    pygame.display.flip()

#Done! Time to quit.
pygame.quit()
