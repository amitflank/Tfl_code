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
        self.has_moved = False

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
        "highlight piece and set it's is_selected property to True"
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
        surf = pygame.image.load(piece_icons[self.color][self.piece_type]).convert()
        surf = pygame.transform.scale(surf, (self.height, self.width))
        surf.set_colorkey((255, 255, 255), RLEACCEL)

        return surf

def get_piece_at_loc(row: int, col: int, pieces: List[Piece]) -> Union[Piece, None]:
    """takes a row and col and return the piece at specified location if it exists. Otherwise return None"""
    for piece in pieces:
        if row == piece.row and col == piece.col:
            return piece

    return None

class Pawn(Piece):

    def __init__(self, height: int, width: int, color: str):
        super().__init__(height, width, "pawn", color)
        self.legal_en_passe = False
    
    def update_en_passe(self, new_row):
        if abs(self.row - new_row) ==  2:
            self.legal_en_passe = True

    def is_legal_move(self, new_row: int, new_col: int, is_capture: bool):
        """checks if given move satisfies legal move conditions for pawn. Does not check for pins or blocked movement"""
        valid_move = True

        if is_capture:
            if self.color is "black":
                valid_row = (new_row == self.row + 1)
            elif self.color is "white":
                valid_row = (new_row == self.row - 1)
            else:
                raise ValueError("got illegal color {0}".format(self.color))
            
            valid_col = abs(new_col  - self.col) == 1
            valid_move = valid_row and valid_col

        else:
            if self.color is "black":
                move = new_row - self.row 
                if self.row == 1:
                    valid_row = move <= 2 and move >= 0 
                else:
                    valid_row = move <= 1 and move >= 0 
                
            if self.color is "white":
                move =  self.row - new_row 

                if self.row == 6:    
                    valid_row =  move  <= 2 and move >= 0 
                else:
                    valid_row = move  <= 1 and move >= 0 
            
            valid_col = (self.col == new_col)
            valid_move = valid_row and valid_col

        return valid_move
    
    def get_move_path(self, new_row: int, new_col: int):
        path = []


        if abs(new_row - self.row) > 1:
            row_unit = (new_row - self.row) // abs(new_row - self.row) 

            for i in range(abs(new_row - self.row)):

                row = self.row + row_unit * (i + 1)
                path.append((row, self.col))
        
        return path

class Bishop(Piece):
    def __init__(self, height: int, width: int, color: str):
        super().__init__(height, width, "bishop", color)

    def is_legal_move(self, new_row: int, new_col: int, is_capture: bool):
        return abs(new_row - self.row) == abs(new_col - self.col)
    
    def get_move_path(self, new_row: int, new_col: int):
        """assumes you have checked legal move so will break if not"""
        row_unit = (new_row - self.row) / abs(new_row - self.row) 
        col_unit = (new_col - self.col) / abs(new_col - self.col)

        path = []

        for i in range(abs(new_row - self.row)):
            row = self.row + row_unit * (i + 1)
            col = self.col + col_unit * (i + 1)
            path.append((row, col))

        return path

class Rook(Piece):
    def __init__(self, height: int, width: int, color: str):
        super().__init__(height, width, "rook", color)
        self.has_moved = False

    def is_legal_move(self, new_row: int, new_col: int, is_capture: bool):
        vertical_move =  abs(new_row - self.row) > 0 and abs(new_col - self.col)  == 0
        horizontal_move = abs(new_row - self.row) == 0  and abs(new_col - self.col) > 0
        return vertical_move or horizontal_move
    
    def get_move_path(self, new_row: int, new_col: int):
        path = []

        if  abs(new_row - self.row) == 0: #horizontal move
            unit_move = (new_col - self.col) / abs(new_col - self.col)

            for i in range(abs(new_col - self.col)):
                col = self.col + unit_move * (i + 1)
                path.append((self.row, col)) #row stays same so we can use self.row for all elements in path
        else:
            unit_move = (new_row - self.row) / abs(new_row - self.row)

            for i in range(abs(new_row - self.row)):
                row = self.row + unit_move * (i + 1)
                path.append((row, self.col)) #col stays same so we can use self.row for all elements in path
        
        return path



class Queen(Piece):
    def __init__(self, height: int, width: int, color: str):
        super().__init__(height, width, "queen", color)
    
    def is_legal_move(self, new_row: int, new_col: int, is_capture: bool):
        diagonal_move = abs(new_row - self.row) == abs(new_col - self.col)
        vertical_move =  abs(new_row - self.row) > 0 and abs(new_col - self.col)  == 0
        horizontal_move = abs(new_row - self.row) == 0  and abs(new_col - self.col) > 0
        return diagonal_move or vertical_move or horizontal_move

    def get_move_path(self, new_row: int, new_col: int):
        """very ugly lot of refactoring potential with reuse across classes and similar code"""
        path = []

        diagonal_move = abs(new_row - self.row) == abs(new_col - self.col)
        vertical_move =  abs(new_row - self.row) > 0 and abs(new_col - self.col)  == 0
        horizontal_move = abs(new_row - self.row) == 0  and abs(new_col - self.col) > 0

        if diagonal_move:
                  
            row_unit = (new_row - self.row) / abs(new_row - self.row) 
            col_unit = (new_col - self.col) / abs(new_col - self.col)

            for i in range(abs(new_row - self.row)):
                row = self.row + row_unit * (i + 1)
                col = self.col + col_unit * (i + 1)
                path.append((row, col))
    
        elif horizontal_move:
            unit_move = (new_col - self.col) / abs(new_col - self.col)

            for i in range(abs(new_col - self.col)):
                col = self.col + unit_move * (i + 1)
                path.append((self.row, col)) #row stays same so we can use self.row for all elements in path
        
        elif vertical_move: 
            unit_move = (new_row - self.row) / abs(new_row - self.row)

            for i in range(abs(new_row - self.row)):
                row = self.row + unit_move * (i + 1)
                path.append((row, self.col)) #col stays same so we can use self.row for all elements in path
        else:
            pass #do nothing if we get a bad move
        
        return path

class Knight(Piece):
    def __init__(self, height: int, width: int, color: str):
        super().__init__(height, width, "knight", color)

    def is_legal_move(self, new_row: int, new_col: int, is_capture: bool):
        vertical_move = abs(new_row - self.row) == 2 and abs(new_col - self.col) == 1
        horizontal_move = abs(new_row - self.row) == 1 and abs(new_col - self.col) == 2
        return vertical_move or horizontal_move   

    def get_move_path(self, new_row: int, new_col: int):
        return []

class King(Piece):
    def __init__(self, height: int, width: int, color: str):
        super().__init__(height, width, "king", color)
        self.has_moved = False

    def is_legal_move(self, new_row: int, new_col: int, is_capture: bool):
        return  abs(new_row - self.row) <= 1 and abs(new_col - self.col) <= 1
    
    def get_move_path(self, new_row: int, new_col: int):
        return []

class Board():

    def __init__(self, cell_size: int) -> None:
        self.piece_key_map = {"queen": Queen, "king": King, "pawn": Pawn, "rook": Rook, "knight": Knight, "bishop": Bishop}
        self.turn = "white"
        self.cell_size = cell_size
        self.ROWS = 8
        self.COLS = 8
        self.selected_piece = None

        self.screen = self.set_up_screen(cell_size)
        self.draw_board(cell_size)
        self.pieces = self.load_pieces(cell_size)


    def flip_turn(self):
        if self.turn is "white":
            self.turn = "black"
        else:
            self.turn = "white"
        
    def set_up_screen(self, cell_size):
        """Create our screen object which we will be drawing on"""
        screen = Surface((cell_size * 8, cell_size * 8))

        # Set up the drawing window
        screen = pygame.display.set_mode([cell_size * 8, cell_size * 8])

        #Update the display
        pygame.display.set_caption("ChessBoard")

        return screen

    def draw_tile(self, cell_size: int, screen: Surface, row: int, col: int):
        if row % 2 == col % 2:
            pygame.draw.rect(self.screen, (255,255,255), (col*cell_size, row*cell_size, cell_size, cell_size))
        else:
            pygame.draw.rect(self.screen, (0,0,0), (col*cell_size, row*cell_size, cell_size, cell_size))

    def draw_board(self, cell_size: int):
        """Draws alternating color chessboard with each tile being dims: cell_size by cell_size"""
        for row in range(self.ROWS):
            for col in range(self.COLS):
               self.draw_tile(cell_size, self.screen, row, col)
    
    def load_color(self, cell_size: int, color: str) -> List[Piece]:
        """Loads all the starting pieces of specified color for start of the game. Returns a list all pieces (not ordered)"""
        piece_list = []
        for piece, loc in my_pieces[color]["position"].items():
            for row, col in loc:
                new_piece = self.piece_key_map[piece](cell_size, cell_size, color) #create piece
                new_piece.update_cell_position(row, col) #initialize proper board location
                self.screen.blit(new_piece.surf, new_piece.rect) #add to board
                piece_list.append(new_piece)
        
        return piece_list
    
    def load_pieces(self, cell_size) -> List[Piece]:
        """Loads all the starting pieces for start of the game. Returns a list all pieces (not ordered)"""
        black_pieces = self.load_color(cell_size, color = "black")
        white_pieces = self.load_color(cell_size, color = "white")

        return black_pieces + white_pieces


    def handle_selection(self, piece: Piece) -> bool:
        """handles piece selection and highlighting, returns a boolean if this is a capture attempt"""
        if piece.color is self.turn:

            if self.selected_piece:
                self.selected_piece.de_select(self.screen)
            
            self.selected_piece = piece
            piece.select(self.screen)
            return False
        else: #indicate a capture attempt
            if self.selected_piece:
                return True
    
    def get_unblocked_path(self, row: int, col: int, piece: Piece):
        path = piece.get_move_path(row, col)
        unblocked_path = []

        for cur_row, cur_col in path:
            blocking_piece = get_piece_at_loc(cur_row, cur_col, self.pieces)

            if blocking_piece:
                if blocking_piece.color is not piece.color:
                    #if piece color doesn't match we can capture so it's valid and added . 
                    #We check pawn excpetion in it's move logic so we don't have a bug here for that special case
                    unblocked_path.append((cur_row, cur_col)) 
                break #once we hit a pice we are done 

            unblocked_path.append((cur_row, cur_col))

        return unblocked_path


    def location_unblocked(self, row: int, col: int, piece: Piece):
        path = piece.get_move_path(row, col)

        if not path: #if list is empty this piece doesn't care about blockers
            return True
        else:
            legal_path = self.get_unblocked_path(row, col, piece)
            return (row, col) in legal_path

    def update_pawn_en_passe_status(self):
        for piece in self.pieces:
            if type(piece) is Pawn and piece.color == self.turn:
                piece.legal_en_passe = False

    def check_en_passe(self, row, col):
        cap_row = row
        if type(self.selected_piece) is Pawn:
            if self.turn is "black":
                cap_row -= 1
            else:
                cap_row += 1

            print(cap_row, self.turn)
            piece = get_piece_at_loc(cap_row, col, self.pieces)
            if piece:
                print(piece)
                return type(piece) is Pawn and piece.legal_en_passe
            
            return False
        return False

    def en_passe_capture(self, row) -> int:
        cap_row = row
        if self.turn is "black":
            cap_row -= 1
        else:
            cap_row += 1
        return cap_row

    def move_selected_piece(self, row: int, col: int, is_capture: bool, is_en_passe: bool):
        cur_row, cur_col = self.selected_piece.row, self.selected_piece.col
        location_unblocked = self.location_unblocked(row, col, self.selected_piece)

        if self.selected_piece.is_legal_move(row, col, is_capture) and location_unblocked:
            #delete a piece if it gets captured
            if is_capture:
                cap_row = row
                if is_en_passe:
                    cap_row = self.en_passe_capture(row)

                self.draw_tile(self.cell_size, self.screen, cap_row, col)
                piece = get_piece_at_loc(cap_row, col, self.pieces)
                self.pieces.remove(piece)
            
            if type(self.selected_piece) is Pawn:
                self.selected_piece.update_en_passe(row)
            
            self.selected_piece.update_cell_position(row, col) #initialize proper board location

            self.screen.blit(self.selected_piece.surf, self.selected_piece.rect) #add to board
            self.draw_tile(self.cell_size, self.screen, cur_row, cur_col)
            self.selected_piece.de_select(self.screen)
            self.selected_piece = None #deselect piece
            self.flip_turn() #other player turn now
            self.update_pawn_en_passe_status() #we reset en passe status at start of turn

pygame.init()

cellSize = 100
new_board = Board(cellSize)

# Run until the user asks to quit
running = True

new_board.load_pieces(cellSize)

while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Get mouse click event
        if event.type == pygame.MOUSEBUTTONDOWN:
            col_pos, row_pos = pygame.mouse.get_pos()
            is_capture = False
            is_en_passe = False

            col = int(col_pos / cellSize)
            row = int(row_pos / cellSize)
            
            piece = get_piece_at_loc(row, col, new_board.pieces) #check if there is a piece at mouseclick location

            if piece:
                is_capture = new_board.handle_selection(piece)
                if is_capture:
                    new_board.move_selected_piece(row, col, is_capture, is_en_passe)
            else:
                if new_board.selected_piece:
                    is_en_passe = new_board.check_en_passe(row, col)
                    if is_en_passe:
                        new_board.move_selected_piece(row, col, True, is_en_passe)
                    else:
                        new_board.move_selected_piece(row, col, is_capture, is_en_passe)

    pygame.display.flip()

#Done! Time to quit.
pygame.quit()
