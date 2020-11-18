public class test
{
    public void useAccount()
    {
        Account account_1;
        
        account_1 = new Account("Fred");
        
        account_1.print();
        account_1.deposit(200);
        account_1.print();
        account_1.withdraw(125);
        account_1.print();
    }
}
