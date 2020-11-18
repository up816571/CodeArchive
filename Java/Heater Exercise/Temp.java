public class Temp
{
    private int temperature;
    private int minimum;
    private int maximum;
    private int increment;
    private double thing;
    
    public Temp(int Max, int Min)
    {
        maximum = Max;
        minimum = Min;
        increment = 5;
        temperature = 15;
    }
    
    public int getTemp()
    {
        return temperature;
    }
    
    public void changeInc(int newInc)
    {
        if (newInc > 0)
            increment = newInc;
        else
            System.out.println("Please enter a positive number");
    }
    
    public void warmer()
    {
        if ((temperature + increment) <= maximum)
        {
            temperature += increment;
        }
        else
        {
            System.out.println("Too hot");
        }
    }
    
    public void cooler()
    {
        temperature -= increment;
        if ((temperature - increment) >= minimum) 
        {
            temperature -= increment;
        }
        else
        {
            System.out.println("Too cold");
        }
    }
    
}