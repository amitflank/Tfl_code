from typing import List, Union, Tuple
from copy import deepcopy
import itertools

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
        self.attacked_tiles = []
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

    def is_legal_row_and_col(self, row, col):
        """check if passed row and col are both inside a legal chess board"""
        legal_row = (row <= 7 and row >= 0)
        legal_col = (col <= 7 and col >= 0)
        return legal_col and legal_row

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
    
    def get_attacked_tiles(self):
        a = 1

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
    
    def get_attacked_tiles(self, board = None):
        attacked_tiles = []
        if self.col > 0:
            if self.color is "black":
                attacked_tiles.append((self.row + 1, self.col - 1))
            else:
                attacked_tiles.append((self.row - 1, self.col - 1))

        if self.col < 7:
            if self.color is "black":
                attacked_tiles.append((self.row + 1, self.col + 1))
            else:
                attacked_tiles.append((self.row - 1, self.col + 1))
        
        return attacked_tiles

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
        path = []

        try:
            row_unit = (new_row - self.row) / abs(new_row - self.row) 
            col_unit = (new_col - self.col) / abs(new_col - self.col)

            for i in range(abs(new_row - self.row)):
                row = self.row + row_unit * (i + 1)
                col = self.col + col_unit * (i + 1)
                path.append((row, col))
        
        except ZeroDivisionError:
            pass

        return path
    
    def get_attacked_tiles(self, board, ignore = None, add_loc = None, add_piece = None):
        attacked_tiles = []

        legal_diag_moves = [-1, 1] 
        unit_moves = list(itertools.product(legal_diag_moves, repeat=2))

        for row_move, col_move in unit_moves:
            legal_move = True
            new_row = self.row
            new_col = self.col

            while(legal_move):

                if self.is_legal_row_and_col(new_row + row_move, new_col + col_move):
                    new_row += row_move 
                    new_col += col_move 
                else:
                    legal_move = False

            attacked_tiles += board.get_unblocked_path(new_row, new_col, self, ignore, add_loc, add_piece)

        return attacked_tiles


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

        try:
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
        except ZeroDivisionError:
            pass
            
        return path
    
    #This is such bad design breaks so much game logic and coding principles. piece should net depend on board
    def get_attacked_tiles(self, board, ignore = None, add_loc = None, add_piece = None):
        #make this an iterable loop (lambda fxn) map? want combinations not permutations
        #gets vertical horizontal movement
        attacked_tiles = [] 
        attacked_tiles += board.get_unblocked_path(7, self.col, self, ignore, add_loc, add_piece)
        attacked_tiles +=  board.get_unblocked_path(0, self.col, self, ignore, add_loc, add_piece)
        attacked_tiles +=  board.get_unblocked_path(self.row, 7, self, ignore, add_loc, add_piece)
        attacked_tiles += board.get_unblocked_path(self.row, 0, self, ignore, add_loc, add_piece)

        return attacked_tiles



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

        try:
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

        except ZeroDivisionError:
            pass
            
        return path
    
    #This is such bad design breaks so much game logic and coding principles. piece should net depend on board
    def get_attacked_tiles(self, board, ignore = None, add_loc = None, add_piece = None):
        #make this an iterable loop (lambda fxn) map? want combinations not permutations
        #gets vertical horizontal movement
        attacked_tiles = [] 
        attacked_tiles += board.get_unblocked_path(7, self.col, self, ignore, add_loc, add_piece)
        attacked_tiles +=  board.get_unblocked_path(0, self.col, self, ignore, add_loc, add_piece)
        attacked_tiles +=  board.get_unblocked_path(self.row, 7, self, ignore, add_loc, add_piece)
        attacked_tiles += board.get_unblocked_path(self.row, 0, self, ignore, add_loc, add_piece)

        legal_diag_moves = [-1, 1] 
        unit_moves = list(itertools.product(legal_diag_moves, repeat=2))

        for row_move, col_move in unit_moves:
            legal_move = True
            new_row = self.row
            new_col = self.col

            while(legal_move):

                if self.is_legal_row_and_col(new_row + row_move, new_col + col_move):
                    new_row += row_move 
                    new_col += col_move 
                else:
                    legal_move = False

            attacked_tiles += board.get_unblocked_path(new_row, new_col, self, ignore, add_loc, add_piece)

        return attacked_tiles

class Knight(Piece):
    def __init__(self, height: int, width: int, color: str):
        super().__init__(height, width, "knight", color)

    def is_legal_move(self, new_row: int, new_col: int, is_capture: bool):
        vertical_move = abs(new_row - self.row) == 2 and abs(new_col - self.col) == 1
        horizontal_move = abs(new_row - self.row) == 1 and abs(new_col - self.col) == 2
        return vertical_move or horizontal_move   

    def get_move_path(self, new_row: int, new_col: int):
        return []

    def get_attacked_tiles(self, board = None):
        attacked_tiles = []
        legal_moves = [-2, -1, 1, 2] #legal row col move values for a knight
        output_list = list(itertools.product(legal_moves, repeat=2))

        for row, col in output_list:
            new_row = self.row + row 
            new_col = self.col + col

            valid_combo = abs(row) != abs(col)
            if self.is_legal_row_and_col(new_row, new_col) and valid_combo:
                attacked_tiles.append((self.row + row, self.col + col))
        
        return attacked_tiles

class King(Piece):
    def __init__(self, height: int, width: int, color: str):
        super().__init__(height, width, "king", color)
        self.has_moved = False

    def is_legal_move(self, new_row: int, new_col: int, is_capture: bool):
        return  abs(new_row - self.row) <= 1 and abs(new_col - self.col) <= 1
    
    def get_move_path(self, new_row: int, new_col: int):
        return []

    def get_attacked_tiles(self, board = None):
        attacked_tiles = []

        #get all row col combonition of legal king movements
        test_list = [range(-1, 2),range(-1,2)] 
        output_list = list(itertools.product(*test_list))
        output_list.remove((0,0)) # we don't want no movement included

        for row, col in output_list:
            new_row = self.row + row 
            new_col = self.col + col
            if self.is_legal_row_and_col(new_row, new_col):
                attacked_tiles.append((self.row + row, self.col + col))
        
        return attacked_tiles


class Board():

    def __init__(self, cell_size: int) -> None:
        self.piece_key_map = {"queen": Queen, "king": King, "pawn": Pawn, "rook": Rook, "knight": Knight, "bishop": Bishop}
        self.turn = "white"
        self.cell_size = cell_size
        self.ROWS = 8
        self.COLS = 8
        self.selected_piece = None
        self.sorted_pieces = deepcopy(my_pieces)
        self.in_check =  {"white": [], "black": []}

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
        for piece, loc in my_pieces[color].items():
            piece_idx = 0 #ugly
            for row, col in loc:
                new_piece = self.piece_key_map[piece](cell_size, cell_size, color) #create piece
                new_piece.update_cell_position(row, col) #initialize proper board location
                self.screen.blit(new_piece.surf, new_piece.rect) #add to board
                piece_list.append(new_piece)
                self.sorted_pieces[color][piece][piece_idx] = new_piece #very ugly
                piece_idx += 1
        
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
    
    def get_unblocked_path(self, row: int, col: int, piece: Piece, ignore = None, add_loc = None, add_piece = None):
        path = piece.get_move_path(row, col)
        unblocked_path = []

        for cur_row, cur_col in path:
            blocking_piece = get_piece_at_loc(cur_row, cur_col, self.pieces)

            if (cur_row, cur_col) == add_loc:
                blocking_piece = add_piece

            if blocking_piece and (cur_row, cur_col) != ignore:
                if blocking_piece.color is not piece.color:
                    #if piece color doesn't match we can capture so it's valid and added . 
                    #We check pawn excpetion in it's move logic so we don't have a bug here for that special case
                    unblocked_path.append((cur_row, cur_col)) 
                break #once we hit a piece we are done 

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
        """resets en passe status of all pawns of player who turn it currently is"""
        for piece in self.pieces:
            if type(piece) is Pawn and piece.color == self.turn:
                piece.legal_en_passe = False

    def check_en_passe(self, row: int, col: int) -> bool:
        if type(self.selected_piece) is Pawn:
            cap_row = self.en_passe_capture(row)
            piece = get_piece_at_loc(cap_row, col, self.pieces)

            if piece:
                return type(piece) is Pawn and piece.legal_en_passe
            
            return False
        return False

    def en_passe_capture(self, row) -> int:
        """returns row of piece being capture en passe"""
        if self.turn is "black":
            return row - 1

        return row + 1
    
    def get_king_loc(self, color: str) -> Tuple[int, int]:
        """get tuple of row and colum of the king with of color"""
        for piece in self.pieces:
            if type(piece) is King and piece.color == color:
                return piece.row, piece.col

    def update_attacking_pieces(self, ignore = None, add_loc = None, add_piece = None) -> List[Piece]:
        """should update attacking squares of rook, bishop and queen for all colors"""
        
        op_color =  "black" if (self.turn == "white") else "white"
        king_pos = self.get_king_loc(op_color)
        attacks_king = []

        update_types = [Queen, Bishop, Rook]
        for piece in self.pieces:
            if type(piece) in update_types:
                piece.attacked_tiles = piece.get_attacked_tiles(self, ignore, add_loc, add_piece)

            if piece.color == self.turn:
                if king_pos in piece.attacked_tiles:
                    attacks_king.append(piece)

        return attacks_king

    def legal_move_while_in_check(self, row: int, col: int):
        """returns a bool indicating is this is a legal move while in check. If not in check returns True"""
        if len(self.in_check[self.turn]) == 0:
            return True
        elif len(self.in_check[self.turn]) == 1:
            check_piece = self.in_check[self.turn][0]
            check_path = check_piece.get_attacked_tiles(self) #gets path of opposite colored piece attacking king

            #if king moves must be out of check path if another piece moves must be into check path or removing checking piece
            if type(self.selected_piece) is King:
                return (row, col) not in check_path
            else:
                return (row, col) in check_path or (row, col) == (check_piece.row, check_piece.col)
        else: # only other option is 2 pieces in this case king must move since we cannot block both
            if type(self.selected_piece) is King:
                check_path = self.in_check[self.turn][0] + self.in_check[self.turn][1]
                return (row, col) not in check_path
            return False
    
    def pawn_promotion(self, piece: Pawn):
        """For simplicity we will only allow queen promotions as this is the most common case, we may update this in future.
        called on pawn movement. Replaces pawn with queen of appropriate color on same square if pawn reaches final row"""
        row, col = piece.row, piece.col
        if type(piece) is not Pawn:
            raise ValueError("pawn promotion only accepts pieces of type pawn but received piece of type {0}".format(type(piece)))
        
        if piece.color is "black" and row == 7 or piece.color is "white" and row == 0:
            new_queen = Queen(self.cell_size, self.cell_size, piece.color)
            self.pieces.remove(piece)
            new_queen.update_cell_position(row, col)
            self.pieces.append(new_queen)
            self.selected_piece = new_queen

    #def castle:
    #   if king has not moved and closest rook has not moved implement some logic to move both
    #   king can not move through check but rook can
    #   use variant of method that checks for checks (I know awkward lang) to see if tile being moved through are being attacked

    def is_checkmate(self) -> bool:
        k_row, k_col = self.get_king_loc(self.turn)
        king: King =  get_piece_at_loc(k_row, k_col, self.pieces)

        legal_king_move = False
        legal_blocker = False

        #check if king has legal move that removes it from check
        attacking_piece = self.in_check[self.turn][0]
        potential_tiles = king.get_attacked_tiles()
            
        for row, col in potential_tiles:
            new_pos = row, col
            if self.location_unblocked(row, col, king):
                if new_pos not in attacking_piece.get_attacked_tiles(self):
                    legal_king_move = True

        if len(self.in_check[self.turn]) == 1:

            #going to need some special condition checks for pawn behavior not mathching attacking behavior
            return legal_king_move or legal_blocker
        else:
            return legal_king_move

    def is_illegal_check(self, color: str, ignore: tuple, add_loc: tuple, add_piece: Piece) -> bool:
        """returns a bool indicating if this move causes king to illegally be placed in check"""
        king_pos = self.get_king_loc(color)

        update_types = [Queen, Bishop, Rook]
        for piece in self.pieces:
            if type(piece) in update_types and (piece.color is not color):
                if king_pos in piece.get_attacked_tiles(self, ignore, add_loc, add_piece):
                    return True
        
        return False
                    
    def move_selected_piece(self, row: int, col: int, is_capture: bool, is_en_passe: bool):
        cur_row, cur_col = self.selected_piece.row, self.selected_piece.col 
        location_unblocked = self.location_unblocked(row, col, self.selected_piece)
        illegal_check = self.is_illegal_check(self.turn, (cur_row, cur_col), (row, col), self.selected_piece)
        legal_if_in_check = self.legal_move_while_in_check(row, col)

        if self.selected_piece.is_legal_move(row, col, is_capture) and location_unblocked and not illegal_check and legal_if_in_check:
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

            if type(self.selected_piece) is Pawn:
                self.pawn_promotion(self.selected_piece)
            
            self.selected_piece.attacked_tiles = self.selected_piece.get_attacked_tiles(self)
            attacks_king = self.update_attacking_pieces()
            self.in_check[self.turn] = [] # we passed legal check move so we reset check status for this color

            self.screen.blit(self.selected_piece.surf, self.selected_piece.rect) #add to board
            self.draw_tile(self.cell_size, self.screen, cur_row, cur_col)
            self.selected_piece.de_select(self.screen)
            self.selected_piece = None #deselect piece
            self.flip_turn() #other player turn now
            
            self.in_check[self.turn] = attacks_king #update check status for opposite color, we run after flip turn so it's not a bug
            self.update_pawn_en_passe_status() #we reset en passe status at start of new turn

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
                        is_capture = True
                    new_board.move_selected_piece(row, col, is_capture, is_en_passe)

    pygame.display.flip()

#Done! Time to quit.
pygame.quit()