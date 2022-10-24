piece_icons = {
    "black": {
        "queen": "piece_pics/queen.png",
        "pawn": "piece_pics/pawn.png",
        "rook": "piece_pics/rook.png",
        "king": "piece_pics/king.png",
        "bishop": "piece_pics/bishop.jpg",
        "knight": "piece_pics/knight.jpeg",
    },
    "white": {
        "queen": "piece_pics/white_queen.jpg",
        "pawn": "piece_pics/white_pawn.png",
        "rook": "piece_pics/white_rook.png",
        "king": "piece_pics/white_king.png",
        "bishop": "piece_pics/white_bishop.jpg",
        "knight": "piece_pics/white_knight.jpeg",
    }
}


my_pieces = {
    "black": {
            "rook": [(0, 0), (0, 7)],
            "knight": [(0, 1), (0, 6)],
            "bishop": [(0, 2), (0, 5)],
            "queen":  [(0, 3)], 
            "king":  [(0, 4)], 
            "pawn": [(1, x) for x in range(8)]
        },
        
    "white": {
            "rook": [(7, 0), (7, 7)],
            "knight": [(7, 1), (7, 6)],
            "bishop": [(7, 2), (7, 5)],
            "queen":  [(7, 3)], 
            "king":  [(7, 4)],
            "pawn": [(6, x) for x in range(8)]
        }
    }