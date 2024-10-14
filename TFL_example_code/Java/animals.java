//Import a library to get access to additional useful methods and classes
import java.util.*;
import java.lang.Math;
import java.lang.IllegalArgumentException;
import java.lang.System;


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

	public boolean isAlive(){
		return isAlive;
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

	public Herbivore(int moveCost, int meatVal){
		super(moveCost);
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

	public Carnivore (int moveCost) {
		super(moveCost);
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
	int growthRate;
	Plant plant;

	public Tile(int growthRate){
		Random rand = new Random(System.currentTimeMillis());
		this.growthRate = rand.nextInt(10);
		this.growthRate = growthRate;
		plant = new Plant(growthRate);
	}

	public void addAnimal(Animal animal){
		this.contains.add(animal);
	}

	public static boolean isHerb(Object obj){
		return "Herbivore".equals(obj.getClass().getName());
	}

	public static boolean isCarni(Object obj){
		return "Carnivore".equals(obj.getClass().getName());
	}

	public int[] get_num_by_type_animals() throws IllegalArgumentException{
		int animal_quant[] = new int[2];
		int herb = 0;
		int carni =0;

		for(int i = 0; i< contains.size(); i++){
			if (Tile.isHerb(contains.get(i))) //check if current animal is herbivore
				herb += 1;
			else if (Tile.isCarni(contains.get(i))) 
				carni += 1;
			else 
				throw new IllegalArgumentException("Found illegal non-animal in Tile contains");
		}

		animal_quant[0] = herb;
		animal_quant[1] = carni;
		return animal_quant;
		
		}
	}

	/** Represents game board in which all of our activities will take place. */
	class Board{
		private int minBoardSize = 6;
		private int boardDim[] = new int[2];
		private int herbProp[] = new int[4];
		private int carniProp[] = new int[3];
		public int corpseCount = 0;

		private Tile[][] grid;

		public Board(int boardDim[], int herbProp[], int carniProp[], int growthMul){
			this.boardDim[0] = boardDim[0];
			this.boardDim[1] = boardDim[1];

			if (this.boardDim[0] < minBoardSize)
				this.boardDim[0] = minBoardSize;
			if (this.boardDim[1] < minBoardSize)
				this.boardDim[1] = minBoardSize;

			//assign prop values for herbivores and carnivores
			for (int i = 0; i < herbProp.length; i ++) this.herbProp[i] = herbProp[i];
			for (int i = 0; i < carniProp.length; i ++) this.carniProp[i]= carniProp[i];

			this.grid = new Tile[this.boardDim[0]][this.boardDim[1]]; //assign board dimensions
			create_board(growthMul);
			addAnimals();
		}

		private void addAnimals(){
			Random rand = new Random(System.currentTimeMillis());

			for(int i = 0; i < herbProp[0]; i++){
				int row = rand.nextInt(getHeight());
				int col = rand.nextInt(getWidth());

				Herbivore myHerb = new Herbivore(herbProp[1], herbProp[2], herbProp[3]);
				grid[row][col].addAnimal(myHerb);
			}

			for(int i = 0; i < carniProp[0]; i++){
				int row = rand.nextInt(getHeight());
				int col = rand.nextInt(getWidth());

				Carnivore myCarni= new Carnivore(carniProp[1], carniProp[2]);
				grid[row][col].addAnimal(myCarni);
			}
		}
		private void create_board(int growthRate) {
			for(int i = 0; i < getHeight(); i++) {
				for (int j = 0; j < getWidth(); j++){
					this.grid[i][j] = new Tile(growthRate);
				}
			}
		}

		public int getHeight(){
			return this.boardDim[0];
		}

		public int getWidth(){
			return this.boardDim[1];
		}

		public int[] getRemainingAnimals() {
			int totalHerb = 0, totalCarni = 0;

			for (int i = 0; i < getHeight(); i ++){
				for (int j = 0; j < getWidth(); j++){
					int rAni[] = grid[i][j].get_num_by_type_animals();
					totalHerb += rAni[0];
					totalCarni += rAni[1];
				}
			}
			return new int[]{totalHerb, totalCarni};
		}

		/**remove dead animals from out game and increase corpse count for each removed animal**/
		private void cleanCorpses(Tile tile){
			int removed_animals = 0;
			ArrayList<Animal>  animals = tile.contains;

			for (int i = 0; i < animals.size(); i++){
				if (!animals.get(i).isAlive()){
					animals.remove(i);
					removed_animals++;
					i--; 
				}
			}
			corpseCount += removed_animals;
		}

		/**
		 * Find the first living herbivore in the list if it exists.
		 * @return Herbivore is it exists, otherwise null
		 */
		private  Optional<Herbivore> getFirstHerbivore(ArrayList<Animal>  animals){
			for (int i = 0; i < animals.size(); i++){
				if (Tile.isHerb(animals.get(i)) && animals.get(i).isAlive()){
					return Optional.ofNullable((Herbivore) animals.get(i));
				}
			}
			return Optional.empty();
		}

		/**Have all animals in passed animals list try and eat as specified by their animal type.
		 * Tile is used to extract plant for herbivores.
        Removes any dead animals from game after feeding is complete**/
		private void feedAnimals(ArrayList<Animal> animals, Tile tile) {
			for (int i = 0; i < animals.size(); i++){
				if (Tile.isHerb(animals.get(i))){
					
					if (animals.get(i).isAlive())
						((Herbivore) animals.get(i)).eat(tile.plant); //Our if statement means we know this is a Herbivore so legal
				}
				else{
					Optional<Herbivore> bambi = getFirstHerbivore(animals);

					if (bambi.isPresent()) {
						((Carnivore) animals.get(i)).eat(bambi.get().getEaten());
					}
				}
			}
			cleanCorpses(tile);
		}

		public boolean coinFlip(){
			Random rand = new Random(System.currentTimeMillis());
			return rand.nextInt(100) < 50; 
		}

		/** Have passed animal move some legal random distance b/w 0 and it's max distance.
			x_cord and y_cord represent animals current location used to help validate legality of animal movement.
			Returns tuple of x_dist, y_dist, total_distance to help with unit testing*/
		public int[] move_animal(Animal animal, int x_cord, int y_cord){
			Random rand = new Random(System.currentTimeMillis());
			
			int max_move = animal.maxMove + 1; //want max move included as option
			int distance = rand.nextInt(max_move); 
			int x_dist = rand.nextInt(distance + 1);

			if (coinFlip())
				x_dist *= -1;

			int abs_y_dist = distance - Math.abs(x_dist);
			int y_dist = abs_y_dist;

			if (coinFlip()) 
				y_dist *= -1;
		   
			
			x_dist = validate_move(x_dist, x_cord, getWidth());
			y_dist = validate_move(y_dist, y_cord, getHeight());
	
			return new int[]{x_dist, y_dist, distance};
	
		}

		/** Move all animals on tile x_cord, y_cord, some random distance. 
			returns list of tuple for x distance traveled, y distance traveled and total distance traveled for testing*/
		public ArrayList<int[]> moveAllAnimalsOnTile(ArrayList<Animal> animals, int x_cord, int y_cord){

			ArrayList<int[]> distances = new ArrayList<int[]>();
			
			for (int i = 0; i < animals.size(); i++){
				if (!animals.get(i).hasMoved){
					int[] values = move_animal(animals.get(i), x_cord, y_cord);
					int x_dist = values[0], y_dist = values[1], distance = values[2];
					animals.get(i).move(distance);

					if (distance != 0){

						grid[y_cord + y_dist][x_cord +x_dist].addAnimal(animals.get(i));
						animals.remove(i);
						cleanCorpses(grid[y_cord + y_dist][x_cord +x_dist]);
						i--;
					}
					distances.add(new int[]{x_dist, y_dist, distance});
				}
			} 
			return distances;
		}

		/** Check if move is valid if not flip direction of move otherwise do nothing*/
		private int validate_move(int move_dist, int cur_pos, int max_val) {
			if (cur_pos + move_dist >= max_val || cur_pos + move_dist <0)
				return -move_dist;
			return move_dist;
		}

		/**reset movement properties of animals so that can legally move on next day */
		private void reset_animal_movement(){
			for (int row = 0; row < getHeight(); row++){
				for (int col = 0; col < getWidth(); col++){
					ArrayList<Animal> animals = grid[row][col].contains;

					for(int i = 0; i < animals.size(); i++){
						animals.get(i).resetMove();
					}
				}
			}
		}

		/**loop over all tiles, have all plants on all tiles grow, have all animals try and eat as specified by animal type then
        move all animals some legal random distance b/w 0 and max_movement*/
		public void cycle_day(){
			Random rand = new Random(System.currentTimeMillis());

			for (int row = 0; row < getHeight(); row++){
				for (int col = 0; col < getWidth(); col++){
					Tile curTile = grid[row][col];
					int growthRate = rand.nextInt(5) + 1; //Want to exclude 0 
					curTile.plant.grow(growthRate);

					feedAnimals(curTile.contains, curTile);
					
					//We can't actually eat after movement b/c we can move in any direction so some animals may miss feeding time if we do
					//we would need to loop again. This is allowed but an interesting design decision. I like keeping my O(n) low so I'll flip it.
					moveAllAnimalsOnTile(curTile.contains, row, col);
				}
			}
			reset_animal_movement();
		}
	} 

	/**Main method for this game. asks user for starting conditions, runs simulation and reports results */
	class PlayGame{
		public static void main(String[] args) {
			Scanner myScan = new Scanner(System.in);
			System.out.println("please enter a board height: ");
			int height = Integer.parseInt(myScan.next()); // We wont worry about error handling

			System.out.println("please enter a board width: ");
			int width = Integer.parseInt(myScan.next()); 

			System.out.println("please enter how many herbivores you would like: ");
			int numHerb = Integer.parseInt(myScan.next());
			
			System.out.println("please enter how many calories herbivores should start with: ");
			int herbCal = Integer.parseInt(myScan.next());

			System.out.println("please enter how many calories it takes a herbivore to move: ");
			int herbMove = Integer.parseInt(myScan.next());

			System.out.println("please enter how many calories consuming a herbivore provides: ");
			int herbMeatVal = Integer.parseInt(myScan.next());

			System.out.println("please enter how many carnivores you would like: ");
			int numCarni = Integer.parseInt(myScan.next());

			System.out.println("please enter how many calories carnivore should start with:");
			int carniCal = Integer.parseInt(myScan.next());

			System.out.println("please enter how many calories it takes a carnivore to move: ");
			int carniMove = Integer.parseInt(myScan.next());

			System.out.println("please enter a number of days to run: ");
			int days = Integer.parseInt(myScan.next());

			System.out.println("please enter scaling value for plant growth rate: ");
			int growthMul = Integer.parseInt(myScan.next());

			int boardDim[] = new int[]{height, width};
			int herbProp[] = new int[]{numHerb, herbCal, herbMove, herbMeatVal};
			int carniProp[] = new int[]{numCarni, carniCal, carniMove};


			Board myBoard = new Board(boardDim, herbProp, carniProp, growthMul);
			for (int i = 0; i < days; i++){
				myBoard.cycle_day();
			}

			int[] tmp = myBoard.getRemainingAnimals();
			int herbsLeft = tmp[0], carniLeft = tmp[1];
	
			String out= String.format("After %d days we killed %d animals and have %d herbivores and %d carnivores left", 
			days, myBoard.corpseCount, herbsLeft,carniLeft);
			System.out.println(out);

 	       	myScan.close();
		}
	}
