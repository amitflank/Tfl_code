//Import a library to get access to additional useful methods and classes
import java.util.*;
import java.lang.Math;
import java.lang.IllegalArgumentException;
import java.lang.System;


class Food {
	//String foodType;
	//int calVal;


	//public Food(String foodType){
    //assign class variable foodtype
    //}

    
	//public String getFood(){
    //return class variable foodTyp
    //}
	
}


class Plant extends Food{
	//int calVal = 0;
	//int growthMul;
	

	//Public Plant(int growthMul) {
        //call parent constructor with foodType "Plant"
        //assign class variable growthMul
    // } 

	//public void grow(int growthRate) {
	//	assign class variable calVal to growthMul * growthRate;
	//}


	//public int grazed() {
    // Set calVal to 0 and return original number of calories
	//}
}

class Meat extends Food{
	//private int calVal;

	//public Meat(int calVal) {
		//call parent constructor with foodType "Plant"
        //assign class variable calVal
	//}

    
	//public int getCalVal(){
		//return calVal
	//}
}

/**Parent class of all movable creatures on our game board. Note Animal is a abstract class so we cannot create instances of this class or call non-static methods.
 * Instead to access Animal features we will need to create instances of it's daughter classes. 
 * @param moveCost  calories cost of moving a tile for this animal.
 * @param calVal    current calories available for animal to take actions
 * @param maxMove   maximum number of tile this animal can move in a day
 * @param isAlive   
 * @param hasMoved

**/
abstract class Animal{

	//int moveCost;
    //int calVal = 100;
	//int maxMove = 3;
	//boolean isAlive = true;
	//boolean hasMoved = false; 

	//We can use constructor overloading to allow for default values for some of our class variables.
	//public Animal(int moveCost) {
        //set class parameter moveCost
	//}

	//public Animal(int moveCost, int calVal) {
		//set class parameter moveCost
		//set class parameter calVal
	//}

	//public Animal(int moveCost, int calVal, int maxMove) {
		//set class parameter moveCost
		//set class parameter calVal
        //set class parameter moveMove
	//}

	//public boolean isAlive(){
		//return if this animal is still alive
    //}

	/**reduce animal calories based on distance traveled and kill it if calories are <= 0 post move **/
	//public void move(int dist){
	//} 

	//public void resetMove() {
        //set animal hasMoved property to false
	//}

}

/**Represents an animal that only eats Plants.
 * 
 **/ 
class Herbivore extends Animal{
	//int meatVal;

	//public Herbivore(int moveCost, int meatVal){
        //set class parameter moveCost
        //set class parameter meatVal
        //have rest of class properties assigned to defaults (Hint use super for assignments)
	//}

	//public Herbivore (int calVal, int moveCost,int meatVal) {
        //set class parameter calVal
        //set class parameter moveCost
        //set class parameter meatVal
         //have rest of class properties assigned to defaults
	//}

	//public Herbivore (int calVal, int moveCost, int max_move, int meatVal) {
        //set class parameter calVal
        //set class parameter moveCost
        //set class parameter maxMove
        //set class parameter meatVal
         //have rest of class properties assigned to defaults
	//}

	//public void eat (Plant plant){
        //add calories stored in plant to calVal
	//}

	//public Meat getEaten(){
        //set isAlive property to false
        //return a new Meat object with meatVal calories
	//}
}

/**Represents an animal that only eats meat.
 * 
 **/ 
class Carnivore extends Animal {

	//public Carnivore (int moveCost) {
		//Assign moveCost and have rest of class properties assigned to default
	//}

	//public Carnivore (int calVal, int moveCost) {
        //Assign class property  moveCost
        //Assign class property calVal
        //have rest of class properties assigned to defaults
	//}

	//public Carnivore (int calVal, int moveCost, int max_move) {
        //Assign class property  moveCost
        //Assign class property calVal
        //Assign class property maxMove
        //have rest of class properties assigned to defaults
	//}

	//public void eat(Meat food){
        //add calories in food to property calVal
	//}
}

class Tile {
	//ArrayList<Animal> contains = new ArrayList<Animal>(); 
	//int growthRate;
	//Plant plant;

	//public Tile(int growthRate){
        //Use random library to get a random int in range [0,10). Seed your random number generator with current time. 
        //assign class property growthRate
        //assign class property plant with new Plant instance with growthRate.

	//}

	//public void addAnimal(Animal animal){
        //Add animal to class ArrayList contains
	//}

	public static boolean isHerb(Object obj){
		return "Herbivore".equals(obj.getClass().getName());
	    }

	public static boolean isCarni(Object obj){
		return "Carnivore".equals(obj.getClass().getName());
	    }
    }
	//public int[] get_num_by_type_animals() throws IllegalArgumentException{
    //return a int array of size where arr[0] = number of herbivores in Tile and 
    //arr[1] contains number of carnivores.
    //Throw a IllegalArgumentException if you encounter anything that is not a herbivore of carnivore
	//}

	/** Represents game board in which all of our activities will take place. */
	class Board{
		//private int minBoardSize = 6;
		//private int boardDim[] = new int[2];
		//private int herbProp[] = new int[4];
		//private int carniProp[] = new int[3];
		//public int corpseCount = 0;

		//private Tile[][] grid;

		//public Board(int boardDim[], int herbProp[], int carniProp[], int growthMul){
            //assign boardDim values
            //If any boardDim value would be less then minBoardSize set it to minBoardSize instead
            //Assign values to class properties herbProp and carniProp
            //Assign our grid property to be a 2D array with dimensions [this.boardDim[0], this.boardDim[1]]
            //create our board with appropriate growthMul. Hint: some other methods may be useful here
            //add animals to board. Hint: some other methods may be useful here
		//}

		//private void addAnimals(){
			//The First value of herbProp is the number of herbivores on the board
			//The First value of carniProp is the number of carnivores on the board
			//The Remaining values of herbProp and carniProp are the properties of the animals matching those in their respective classes
            //add appropriate number of herbivores and carnivores to our board as defined by 
            //herbProp and carniProp. 
            //properties of Herbivores and Carnivores should match those defined 
            //by herbProp and CarniProp
		//}

		//private void create_board(int growthMul) {
            //create new tiles for each index in grid and assign appropriate growthMul to those Tiles.
		//}

        
		//public int getHeight(){
			//return height (number of rows) or out this Board instance. 
		//}

		//public int getWidth(){
			//return width (number of columns) or out this Board instance. 
		//}

		//public int[] getRemainingAnimals() {
            //return int array of size 2 where arr[0] = number of living herbivores left on board
            // and arr[1] = the same for carnivores. 
		//}

		
		//private void cleanCorpses(Tile tile){
            /**remove dead animals from out game and increase corpse count for each removed animal**/
		//}


		//private  Optional<Herbivore> getFirstHerbivore(ArrayList<Animal>  animals){
        /**
		 * Find the first living herbivore in the list if it exists.
		 * @return Herbivore is it exists, otherwise null
		 */

		//}


		//private void feedAnimals(ArrayList<Animal> animals, Tile tile) {
		/**Have all animals in passed animals list try and eat as specified by their animal type.
		 * Tile is used to extract plant for herbivores.
        Removes any dead animals from game after feeding is complete**/
		//}

		//public boolean coinFlip(){
            //return true or false with 50% probability
		//}


		//public int[] move_animal(Animal animal, int x_cord, int y_cord){
		/** Have passed animal move some legal random distance b/w 0 and it's max distance.
			x_cord and y_cord represent animals current location used to help validate legality of animal movement.
			Returns tuple of x_dist, y_dist, total_distance to help with unit testing*/
		//}

		//public ArrayList<int[]> moveAllAnimalsOnTile(ArrayList<Animal> animals, int x_cord, int y_cord){
		/** Move all animals on tile x_cord, y_cord, some random distance. 
			returns list of tuple for x distance traveled, y distance traveled and total distance traveled for testing*/
		//}

		
		//private int validate_move(int move_dist, int cur_pos, int max_val) {
            /** Check if move is valid if not flip direction of move otherwise do nothing*/
		//}

		//private void reset_animal_movement(){
		    /**reset movement properties of animals so that can legally move on next day */
		//}


		//public void cycle_day()
		/**loop over all tiles, have all plants on all tiles grow, have all animals try and eat as specified by animal type then
        move all animals some legal random distance b/w 0 and max_movement. Finally once you have looped over every tiles reset all 
        remaining animal movement for next day.*/
	} 

	
	class PlayGame{
		//public static void main(String[] args) {
			/**Main method for this game. asks user for starting conditions, runs simulation and reports results
             * Hint use Scanner class.
             */
        //}
    }