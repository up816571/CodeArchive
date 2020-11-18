import java.awt.*;

/**
 * Write a description of class Bumper here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */

public class Holes extends PinballObject
{
    public Holes(int xPos, int yPos, int objectRadius, Machine theMachine)
    {
        super(xPos, yPos, 0, 0, Color.BLACK, objectRadius, theMachine);
        theMachine.getHoles().add(this);
    }
    
    public void move()
    {
        machine.erase(this);
        machine.draw(this);
    }
}