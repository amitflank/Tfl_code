import java.util.Random;
import java.util.Scanner;
import java.util.HashSet;
import java.util.Set;

public class AdlibGame {

    public static String selectString(String[] strArr){
        Random random = new Random();
        int index = random.nextInt(strArr.length);
        return strArr[index];
    }

    public static String createRandomSentence(String[] nouns, String[] verbs, String[] adjectives, String[] places, String[] objects) {
        String[] sentenceTemplates = {
            "The " + selectString(adjectives) + " " + selectString(nouns) + " " + selectString(verbs) + " " + selectString(places) + ".",
            "In the " + selectString(places) + ", a " + selectString(adjectives) + " " + selectString(nouns) + " was holding a " + selectString(objects) + ".",
            "A " + selectString(nouns) + " " + selectString(verbs) + " with a " + selectString(adjectives) + " " + selectString(objects) + " in the " + selectString(places) + ".",
            "The " + selectString(nouns) + " quickly " + selectString(verbs) + " with the " + selectString(objects) + " while everyone in the " + selectString(places) + " was watching."
        };
        
        return selectString(sentenceTemplates);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Word lists
        String[] nouns = {"Dragon", "Wizard", "Spaceship", "Robot", "Unicorn", "Ninja", "Pirate", "Alien", "Zombie", "Monster"};
        String[] verbs = {"Dances", "Flies", "Eats", "Jumps", "Builds", "Fights", "Explores", "Discovers", "Chases", "Escapes"};
        String[] adjectives = {"Silly", "Enormous", "Mysterious", "Brave", "Hungry", "Invisible", "Cuddly", "Weird", "Smelly", "Sparkly"};
        String[] places = {"In a haunted castle", "On a distant planet", "Inside a volcano", "At the bottom of the ocean", "In a magical forest",
                           "On a pirate ship", "In a candy factory", "Inside a video game", "At the zoo", "On top of a mountain"};
        String[] objects = {"Laser sword", "Magic wand", "Treasure chest", "Spacesuit", "Golden crown"};

        System.out.println("Please enter a name hit enter if you want to use a random noun");
        String name = scanner.nextLine();
        String names[] = {name};

        //Only runs if user enters a name
        if (!name.isEmpty()) {
            nouns = names;
        }
        

        System.out.println("How many sentences would you like to generate?");
        int sentenceCount = scanner.nextInt();
        Set<String> uniqueSentences = new HashSet<>();

        for (int i = 0; i < sentenceCount; i++) {
            
            String newSentence = createRandomSentence(nouns, verbs, adjectives, places, objects);
            if (uniqueSentences.add(newSentence)) {
                System.out.println(newSentence);
            }
        }

        scanner.close();
    }
}
