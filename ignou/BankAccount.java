public class BankAccount {
    // Private variable: hidden from outside classes
    private double balance;

    // Public method to safely access the private variable
    public void deposit(double amount) {
        if(amount > 0) balance += amount;
    }
}
