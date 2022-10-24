//Import a library to get access to additional useful methods and classes
import java.util.ArrayList;
import java.util.Random;
import java.lang.IllegalArgumentException;

class Food {
	String foodType;
	int calVal;

	public Food(String foodType) {
		this.foodType = foodType;
  	}

	public String getFood() {
    	return this.foodType;
	}
	
}

class Plant extends Food{
	int calVal = 0;
	int growthMul;
	

	public Plant(int growthMul) {
		super("Plant");
        this.growthMul = growthMul;
  	} 

	public void grow(int growthRate) {
		this.calVal += this.growthMul * growthRate;
	}

	public int grazed() {
		int gCal = this.calVal;
		this.calVal -= this.calVal;
		return gCal;
	}
}

class Meat extends Food{
	private int calVal;

	public Meat(int calVal) {
		super("Meat");
		this.calVal = calVal;
	}

	public int getCalVal(){
		return calVal;
	}
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

	int moveCost;
	int calVal = 100;
	int maxMove = 3;
	boolean isAlive = true;
	boolean hasMoved = false; 

	//We can use constructor overloading to allow for default values for some of our class variables.
	public Animal(int moveCost) {
		this.moveCost = moveCost;

	}
	public Animal(int moveCost, int calVal) {
		this.moveCost = moveCost;
		this.calVal = calVal;
	}

	public Animal(int moveCost, int calVal, int maxMove) {
		this.moveCost = moveCost;
		this.calVal = calVal;
		this.maxMove = maxMove;
	}

	/**reduce animal calories based on distance traveled and kill it if calories are <= 0 post move **/
	public void move(int dist){
		this.calVal -= dist *this.moveCost;
		this.hasMoved = true;

		//animal starved
		if (this.calVal <= 0)
			this.isAlive = false;
	} 

	public void resetMove() {
		this.hasMoved = false;
	}

}

/**Represents an animal that only eats Plants.
 * 
 **/ 
class Herbivore extends Animal{
	int meatVal;

	public Herbivore(int calVal, int meatVal){
		super(calVal);
		this.meatVal = meatVal;
	}

	public Herbivore (int calVal, int moveCost,int meatVal) {
		super(moveCost, calVal);
		this.meatVal = meatVal;
	}

	public Herbivore (int calVal, int moveCost, int max_move, int meatVal) {
		super(moveCost, calVal, max_move);
		this.meatVal = meatVal;
	}

	public void eat (Plant plant){
		this.calVal += plant.grazed();
	}

	public Meat getEaten(){
		this.isAlive = false;
		return new Meat(this.meatVal);
	}
}

/**Represents an animal that only eats meat.
 * 
 **/ 
class Carnivore extends Animal {

	public Carnivore (int calVal) {
		super(calVal);
	}

	public Carnivore (int calVal, int moveCost) {
		super(moveCost, calVal);
	}

	public Carnivore (int calVal, int moveCost, int max_move) {
		super(moveCost, calVal, max_move);
	}

	public void eat(Meat food){
		this.calVal += food.getCalVal();
	}
}

class Tile {
	ArrayList<Animal> contains = new ArrayList<Animal>();
	int growthMul;

	public Tile(int growthMul){
		Random rand = new Random();
		this.growthMul = rand.nextInt(10);

		this.growthMul = growthMul;
	}

	public void addAnimal(Animal animal){
		this.contains.add(animal);
	}

	public int[] get_num_by_type_animals() throws IllegalArgumentException{
		int animal_quant[] = new int[2];

		int herb = 0;
		int carni =0;

		String herbStr = "Herbivore";
		String CarniStr = "Carnivore";


		for(int i = 0; i< animal_quant.length; i++){
			if (herbStr.equals(this.contains.get(i).getClass().getName())) { //check if current animal is herbivore
				herb += 1;
			}
			else if (CarniStr.equals(this.contains.get(i).getClass().getName())) {
				carni += 1;
			}
			else {
				throw new IllegalArgumentException("Found illegal non-animal in Tile contains");
			}
		}

		animal_quant[0] = herb;
		animal_quant[1] = carni;
		return animal_quant;
		
	}
}
