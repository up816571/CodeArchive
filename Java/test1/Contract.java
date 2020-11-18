public class Contract
{
    private String provider;
    private String accountHolderName;
    private String phoneNumber;
    private double monthlyCost;
    
    public Contract(String providerName, String holderName, String mobNumber, double cost)
    {
        provider = providerName;
        accountHolderName = holderName;
        phoneNumber = mobNumber;
        monthlyCost = cost;
    }
    
    public String getHolderName() 
    {
        return accountHolderName;
    }
    
    public void changeHolderName(String newName)
    {
        accountHolderName = newName;
    }
    
    public double getMonthlyCost()
    {
        return monthlyCost;
    }
    
    public void changeMonthlyCost(double newCost)
    {
        if (newCost > 0)
        {
            monthlyCost = newCost;
            System.out.println("Monthly cost updated to £" + newCost);
        }
        else
        {
            System.out.println("The cost is too low");
        }
    }
    
    public void printAll()
    {
        System.out.println("Phone Contract Information");
        System.out.println("Phone Company: " + provider);
        System.out.println("Account Holder: " + accountHolderName);
        System.out.println("Phone Number: " + phoneNumber);
        System.out.println("Monthly Price: " + monthlyCost);
    }
}