import java.awt.*;

/**
 * Class to demonstrate functionality of the Pinball machine
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Demo
{
    private Machine machine;

    /**
     * Constructor for objects of class Demo
     */
    public Demo()
    {
        machine = new Machine();
    }

    /**
     * Sample demo method - demonstrates what happens when an object rebounds off the left-hand wall
     */
    public void sampleDemo()
    {
        // sample demo
        machine.resetMachine();
        
        PinballObject obj1 = new Pinball1(50, 200, -10, 6, Color.RED, 10, machine);
        PinballObject obj2 = new Pinball1(100, 300, 2, 4, Color.BLUE, 55, machine);
        PinballObject obj3 = new Pinball1(450, 125, -2, -2, Color.YELLOW, 40, machine);
        PinballObject obj4 = new Pinball4(100, 200, 4, -4, Color.MAGENTA, 25, machine);
        
        while(machine.getRunning())
        {
            machine.pauseMachine(); // small delay
            machine.runDemo();
        }
    }
    
    public void sampleDemo2()
    {
        // sample demo
        machine.resetMachine();
        
        PinballObject obj1 = new Pinball4(300, 300, 3, 0, Color.RED, 20, machine);
        PinballObject obj2 = new Bumper(400, 300, 20, machine);
    
        while(machine.getRunning())
        {
            machine.pauseMachine();           // small delay
            machine.runDemo();
        }
    }
    
    public void sampleDemo3()
    {
        // sample demo
        machine.resetMachine();
        
        PinballObject obj1 = new Pinball4(300, 300, 3, 0, Color.RED, 20, machine);
        PinballObject obj2 = new Pinball4(400, 300, -3, 0, Color.RED, 20, machine);
    
        while(machine.getRunning())
        {
            machine.pauseMachine();           // small delay
            machine.runDemo();
        }
    }
}
