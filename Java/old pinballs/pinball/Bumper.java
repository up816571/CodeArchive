import java.awt.*;

/**
 * Write a description of class Bumper here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Bumper extends PinballObject
{
    public Bumper(int xPos, int yPos, int objectRadius, Machine theMachine)
    {
        super(xPos, yPos, 0, 0, Color.GRAY, objectRadius, theMachine);
        theMachine.getBumps().add(this);
    }
    
    public void move()
    {
        machine.erase(this);
        machine.draw(this);
    }
}
