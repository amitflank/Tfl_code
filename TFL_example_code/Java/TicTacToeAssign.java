import java.util.Scanner;

public class TicTacToeAssign {
    private char[][] board;
    private char currentPlayer;
    private static final int SIZE = 3;
    private Scanner scanner;

    public TicTacToeAssign() {
        board = new char[SIZE][SIZE];
        currentPlayer = 'X';  // Player 1 starts with 'X'
        scanner = new Scanner(System.in);
        initializeBoard();
    }

    // Initialize the board with empty spaces
    //Each board tile should be assigned en empty char to start like this: ' '
    private void initializeBoard() {

    }

    // Main game loop
    public void play() {
        boolean gameWon = false;
        int moves = 0;

        //While the game is not won and there are still moves to be made 
        //Display the board
        //Make a move
        //Check if the game has been won
        //If the game has not been won switch the player
        //Increment the number of moves


        //Display the board
        //If the game has been won display the winning player
        //If the game was a draw display that it was a draw


    }

    // Display the current state of the board
    private void displayBoard() {
        System.out.println("Current board:");

        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                System.out.print(board[i][j]);
                if (j < SIZE - 1) System.out.print(" | ");
            }
            System.out.println();
            if (i < SIZE - 1) System.out.println("---------");
        }
    }

    // Prompt the player to make a move
    private void makeMove() {
        boolean validMove = false;

        //While the move is not valid
        while (!validMove) {
            //System.out.println("Player " + currentPlayer + ", enter your move (row and column): ");
            //Get the row and column from the player using scanner
            


            // Check for valid input
            //If the row and column are within the bounds of the board and the tile is empty
            //Set the tile to the current player
            //Set validMove to true
            //Otherwise print that the move is not valid

        }
    }

    // Check if the current player has won the game
    private boolean checkWin() {
        // Check rows, columns, and diagonals for a win
    }

    private boolean checkRows() {
        //Check each row for a win

    }

    private boolean checkColumns() {
        //Check each column for a win
    }

    private boolean checkDiagonals() {
        //Check the diagonals for a win
    }
}