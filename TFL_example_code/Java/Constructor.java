
/**If we want our class to be public it must have the same name as the file it is in */
class Constructor {
    //These are class variables often referred to as "fields" or "properties" of an instance. They exist everywhere inside the class
    //and can be accessed by non-static methods (unless the variable is static as well).
    String id; //Notice we are no assigning any value to these variables as we  will let our constructor handle that.

    //The private modifier prevents access of this variable outside of the class.  
    private int priv;


    //This is a static variable it will be shared across all instances of this class. We can also access 
    //it from the class itself instead of individual instances. We cannot assign this value in a constructor since it does not
    //belong to an instance. 
    static int stat = 10; 

    //the "final" keyword prevents a variable from being modified after assignment. If we try we will get an error.
    //However, we can still delay assignment until a constructor call, in which case we are required to assign it
    //during such a call. This keyword can be useful for constants that don't change such as pi! Though there are 
    //many other use cases
    private final int f1 = 20;
    private final int f2; 

    
    /**This is a constructor, it's basically just a special method with some key differences. <p> 
     * 1. A constructor must have the exact same name as the class. <p>
     * 2. A constructor cannot be static, abstract, final or native. Well discuss some of these later.<p>
     * 3. A constructor does not include a return type.<p>
     * So what exactly is the point of a constructor? It's designed to set up all the information needed for us to
     * use a class instance (i.e it "constructs" the instance for us). Also a constructor is automatically called 
     * on creation of an instance. If you do not have a explicit constructor then java will create an empty constructor
     * that takes no arguments on instance creation. This however means when we create a constructor the empty
     * constructor is no longer available for instance creation. 
     *  
    */
    public Constructor(String id, int priv, int f2){
        this.id = id; // the "this" keyword if used to refer to something that belongs to current instance.
        this.priv = priv;
        this.f2 = f2;
    }


    public int getPriv(){
        return this.priv;
    }
}

class Dreams{

    public static void main(String[] args) {
        Constructor fail = new Constructor("1", 20, 20);
        System.out.println(fail.id);
        System.out.println(fail.getPriv());
    }

}
