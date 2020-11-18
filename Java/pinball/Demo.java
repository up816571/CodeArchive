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
        PinballObject obj2 = new PinballObject(100, 300, 2, 4, Color.BLUE, 55, machine);
        PinballObject obj3 = new PinballObject(450, 125, -2, -2, Color.YELLOW, 40, machine);
        PinballObject obj4 = new PinballObject(100, 200, 4, -4, Color.MAGENTA, 25, machine);
        
        while(machine.getRunning())
        {
            machine.pauseMachine();           // small delay
            obj1.move();
            obj2.move();
            obj3.move();
            obj4.move();
        }
    }
    
    public void sampleDemo2()
    {
        // sample demo
        machine.resetMachine();
        
        PinballObject obj1 = new PinballObject(270, 300, 0, 3, Color.RED, 10, machine);
    
        while(machine.getRunning())
        {
            machine.pauseMachine();           // small delay
            obj1.move();
        }
    }
    
    public void sampleDemo3()
    {
        // sample demo
        machine.resetMachine();
        
        PinballObject obj1 = new PinballObject(310, 400, -2, 3, Color.RED, 10, machine);
        PinballObject obj2 = new PinballObject(280, 400, 2, 3, Color.RED, 10, machine);
        PinballObject obj3 = new PinballObject(240, 400, 2, 3, Color.RED, 10, machine);
        PinballObject obj4 = new PinballObject(220, 400, 2, 3, Color.RED, 10, machine);
        PinballObject obj5 = new PinballObject(260, 400, -2, 3, Color.RED, 10, machine);
        PinballObject obj6 = new PinballObject(280, 400, -2, 3, Color.RED, 10, machine);
        PinballObject obj7 = new PinballObject(300, 400, -2, 3, Color.RED, 10, machine);
        PinballObject obj8 = new PinballObject(320, 400, -2, 3, Color.RED, 10, machine);
    
        while(machine.getRunning())
        {
            machine.pauseMachine();           // small delay
            obj1.move();
            obj2.move();
            obj3.move();
            obj4.move();
            obj5.move();
            obj6.move();
            obj7.move();
            obj8.move();
        }
    }
}
