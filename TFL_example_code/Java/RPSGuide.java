import java.util.Random;
import java.util.Scanner;

public class RPSGuide {

    // Array to store the choices for easy reference
    private static final String[] choices = {"Rock", "Paper", "Scissors"};

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        
        // Get the user's choice using the getUserChoice method.
        System.out.println(getUserChoice(scanner));    
        System.out.println(getComputerChoice(random));    
        // Get the computer's random choice using the getComputerChoice method.
        
        // Determine the winner using the determineWinner method.
        
        // Print a message thanking the user for playing.
    }

    /**
     * Gets the user's choice of "Rock", "Paper", or "Scissors" by asking them to enter 1, 2, or 3.
     * Ensures valid input.
     * 
     * @param scanner The Scanner object for reading input.
     * @return The user's choice.
     */
    private static String getUserChoice(Scanner scanner) {
        System.out.println("Enter your choice:  1 (rock), 2 (paper), or 3 (scissors)");
        int choice = 0;

        while ( (!scanner.hasNextInt() || (choice = scanner.nextInt()) < 1 || choice > 3)) {
            System.out.println("Invalid input. Please enter 1, 2, or 3: ");
            scanner.nextLine(); // Clear the invalid input
        }
    
        return choices[choice -1]; // Placeholder, replace with your logic.
    }

    /**
     * Randomly selects the computer's choice of "Rock", "Paper", or "Scissors".
     * 
     * @param random The Random object for generating the choice.
     * @return The computer's choice.
     */
    private static String getComputerChoice(Random random) {
        int index = random.nextInt(choices.length);
        // Use the Random object to select an index from the choices array.
        // Return the computer's choice.
        return choices[index]; // Placeholder, replace with your logic.
    }

    public static int winner(String userChoice, String computerChoice) {
        boolean userRockWins = userChoice.equals("Rock") && computerChoice.equals("Scissors");
        boolean userPaperWins = userChoice.equals("Paper") && computerChoice.equals("Rock");
        boolean userScissorsWins = userChoice.equals("Scissors") && computerChoice.equals("Paper");
        boolean userWins =  userRockWins || userPaperWins || userScissorsWins;

        if (userChoice.equals(computerChoice)){
            return 0;
        }
        else if (userWins){
            return 1;
        }
        else {
            return -1;
        }
    }
    /**
     * Determines the winner between the user's choice and the computer's choice.
     * 
     * @param userChoice The user's choice.
     * @param computerChoice The computer's choice.
     */
    private static void determineWinner(String userChoice, String computerChoice) {

        // Compare the user's choice and the computer's choice.
        // Print "It's a tie!" if the choices are the same.
        // Print "You win!" if the user's choice beats the computer's choice.
        // Print "You lose!" if the computer's choice beats the user's choice.
    }
}
