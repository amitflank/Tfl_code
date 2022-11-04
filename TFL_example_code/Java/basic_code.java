import java.util.*;
/**Main method for this game. asks user for starting conditions, runs simulation and reports results */
class Learning{
	public static void main(String[] args) {
         //creating random number in range [0, 26) and assign to variable num
        Random rand = new Random(System.currentTimeMillis());
        int num = rand.nextInt(26);

        //Example of calling a static method, notice we use class blueprint rather then an instance.
        System.out.println(Learning.fizzBuzz(15)); 
        System.out.println(Learning.isPal("1551")); 

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

        int strLen = playPal.length();

        boolean validPal = true;
        int backIdx = strLen - 1;
        for (int i =0; i < strLen; i++){

            //for single line if statements we don't need to include curly braces
            if (i >= backIdx)
                break; //break statement used to exit loop early, we could also rewrite this loop as a while loop, give it a try!

            //could we use the == operator with for a String comparison? Why or why not?
            validPal =  validPal && (playPal.charAt(i) == playPal.charAt(backIdx));
            backIdx--;
        }

        return validPal;
    }

}