import java.util.Random;

public class AdlibGame {

    public static String selectString(String[] strArr){
        Random random = new Random();
        int index = random.nextInt(strArr.length);
        return strArr[index];
    }

    public static void createSentence(String[] nouns, String[] verbs, String[] adjectives, String[] places, String[] objects) {
        String[] sentenceTemplates = {
            "The " + selectString(adjectives) + " " + selectString(nouns) + " " + selectString(verbs) + " " + selectString(places) + ".",
            "In the " + selectString(places) + ", a " + selectString(adjectives) + " " + selectString(nouns) + " was holding a " + selectString(objects) + ".",
            "A " + selectString(nouns) + " " + selectString(verbs) + " with a " + selectString(adjectives) + " " + selectString(objects) + " in the " + selectString(places) + ".",
            "The " + selectString(nouns) + " quickly " + selectString(verbs) + " with the " + selectString(objects) + " while everyone in the " + selectString(places) + " was watching."
        };
        
        System.out.println(selectString(sentenceTemplates));
    }
    
    public static void main(String[] args) {
        // Word lists
        String[] nouns = {"Dragon", "Wizard", "Spaceship", "Robot", "Unicorn", "Ninja", "Pirate", "Alien", "Zombie", "Monster"};
        String[] verbs = {"Dances", "Flies", "Eats", "Jumps", "Builds", "Fights", "Explores", "Discovers", "Chases", "Escapes"};
        String[] adjectives = {"Silly", "Enormous", "Mysterious", "Brave", "Hungry", "Invisible", "Cuddly", "Weird", "Smelly", "Sparkly"};
        String[] places = {"In a haunted castle", "On a distant planet", "Inside a volcano", "At the bottom of the ocean", "In a magical forest",
                           "On a pirate ship", "In a candy factory", "Inside a video game", "At the zoo", "On top of a mountain"};
        String[] objects = {"Magic wand", "Treasure chest", "Crystal ball", "Potion", "Map", "Sword", "Key", "Crown", "Amulet", "Book"};


        for(int i = 0; i < 10; i++){
            createSentence(nouns, verbs, adjectives, places, objects);
        }

    }
}
