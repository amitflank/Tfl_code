class BankAccount {
    private int balance;
    String name;

    public BankAccount(String name, int balance){
        this.balance = balance;
        this.name = name;
    }

    public void deposit(int deposit){
        this.balance += deposit;
    }

    public int withdraw(int val){
        if (val < 0){
            System.out.println("Cannot withdraw a negative value you scoundrel you!");
            return 0;
        }

        if (this.balance - val < 0){
            System.out.println("Insufficient funds");
            return 0;
        } 

        this.balance -= val;
        return val;
    }

    public int getBalance(){
        return this.balance;
    }

    public void transfer(BankAccount account, int value){
        this.balance += account.withdraw(value);
    }

    /**transfer money from second account to first account, this is an example of method overloading.
     * @param acc1 BankAccount we are transferring money to
     * @param acc2 BankAccount we are withdrawing money from
     * @param value amount of money being transferred
     */
    public static void transfer(BankAccount acc1, BankAccount acc2, int value){
        acc1.deposit(acc2.withdraw(value));
    }

}

class BankAccountExercise {
    public static void main(String[] args) {
        BankAccount jeff = new BankAccount("Jeff", 200);
        BankAccount sue = new BankAccount("Sue", 100);

        System.out.println(jeff.getBalance());
        System.out.println(sue.getBalance());


        jeff.transfer(sue, 150);
        System.out.println(jeff.getBalance());
        System.out.println(sue.getBalance());

        sue.deposit(100);
        jeff.transfer(sue, 150);

        System.out.println(jeff.getBalance());
        System.out.println(sue.getBalance());

        sue.withdraw(-50);

    }
}