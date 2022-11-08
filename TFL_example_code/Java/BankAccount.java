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

}
