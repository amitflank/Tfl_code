import java.util.*;
/**Main method for this game. asks user for starting conditions, runs simulation and reports results */
class Learning{
	public static void main(String[] args) {
         //creating random number in range [0, 26) and assign to variable num
        Random rand = new Random(System.currentTimeMillis());
        int num = rand.nextInt(26);

        int myVar = 10;
        Learning show = new Learning();

        //Example of calling a static method, notice we use class blueprint rather then an instance.
        System.out.println(Learning.fizzBuzz(15)); 
        System.out.println(Learning.isPal("1551")); 

        //Example of non-static method call
        System.out.println(show.greaterThenN(100));


        }

    /**This is a docstring place it above a function you wish to comment
     * @param num number whose divisibility we are checking 
     * @return Fizz if num divisible 3, Buzz if num divisible 5, FizzBuzz if divisible by both*/    
    public static String fizzBuzz(int num){
        StringBuilder str = new StringBuilder(); //We use StringBuilder so we don't manipulate an immutable like String.

        if (num % 3 == 0) {
            str.append("Fizz");
        }
        if (num % 5 ==0){
            str.append("Buzz");
        }

        return str.toString();
    }
    
    /**Check if passed string is a palindrome (same forward and backwards)*/
    public static boolean isPal(String playPal){

        boolean validPal = true;
        int backIdx = playPal.length() - 1;  
        for (int i=0; i < playPal.length(); i++, backIdx--){ // we can stack multiple operations in increment step

            //for single line if statements we don't need to include curly braces
            if (i >= backIdx)
                break; //break statement used to exit loop early, we could also rewrite this loop as a while loop, give it a try!

            //could we use the == operator with for a String comparison? Why or why not?
            validPal =  validPal && (playPal.charAt(i) == playPal.charAt(backIdx)); // we could also rewrite this as an if statement
        }

        return validPal;
    }

    /**Keep adding values b/w [0, 10) to a sum until it is greater than passed val*/
    public int greaterThenN(int n){
        Random rand = new Random(System.currentTimeMillis());
        int sum = 0;

        while (sum <= n){
            int num = rand.nextInt(10);
            sum += num;
        }

        return sum;
    }

    /**checks if all numbers are greater than N, if num does not equal zero we still return true as long as number
     * of numbers less then N does not exceed num
     */
    public boolean isGtN(int[] myArr, int num, int N){
        int numGtN = 0;

        for(int i = 0; i < myArr.length;i++){
            if (myArr[i] > N)
                numGtN++;
        }
        return numGtN <= num;

    }

    /**return the absolute value of a number*/
    public static int abs(int val){
        if (val < 0)
            return val *= -1;  
        return val;
    }

    /**return num to the power of power */
    public static int pow(int num, int power){
        int val = 1;
        for(int i =0; i < power; i++){
            val *= num;
        }
        return val;
    }
}