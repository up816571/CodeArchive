

public class Account
{
    
    private String owner;
    private int balance;
    
    public Account(String name)
    {
        owner = name;
        balance = 0;
    }
    
    public void deposit(int anAmount)
    {
        balance += anAmount;
    }
    
    public int withdraw(int anAmount)
    {
        int amountWithdrawn;
        
        if (anAmount <= balance)
            amountWithdrawn = anAmount;
        else
            amountWithdrawn = balance;
            
        balance -= amountWithdrawn;
        
        return amountWithdrawn;
    }
    
    public void print()
    {
        System.out.println("Owner = " + owner + "  Balance = " + balance);
    }
}
    