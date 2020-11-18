import java.awt.*;

/**
 * An object that exists in the pinball. 
 * 
 * Movement can be initiated by repeated calls to the "move" method.
 * 
 * N.B This class is incomplete and still under development. It will require updating to
 * complete the INTPROG coursework assignment.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 * 
 */

public class PinballObject
{
    protected int currentXLocation;
    protected int currentYLocation;
    protected int speedXTravel;
    protected int speedYTravel;
    protected Color colour;
    protected int radius;
    protected Machine machine;
    protected final int leftWallPosition;
    protected final int rightWallPosition;
    protected final int topWallPosition;
    protected final int bottomWallPosition;
    protected final int lengthToGap;
    protected final int gapWidth;
    protected boolean hasHitWall;

    /**
     * Constructor for objects of class Pinball_Obj
     * 
     * @param xPos  the horizontal coordinate of the object
     * @param yPos  the vertical coordinate of the object
     * @param xVel  the horizontal speed of the object
     * @param yVel  the vertical speed of the object
     * @param objectRadius  the radius (in pixels) of the object
     * @param objectColor  the color of the object
     * @param theMachine  the machine this object is in
     */
    public PinballObject(int xPos, int yPos, int xVel, int yVel, Color objectColor, int objectRadius, Machine theMachine)
    {
        currentXLocation = xPos;
        currentYLocation = yPos;
        speedXTravel = xVel;
        speedYTravel = yVel;
        colour = objectColor;
        radius = objectRadius;
        machine = theMachine;
        leftWallPosition = machine.getLeftWall();
        rightWallPosition = machine.getRightWall();
        topWallPosition = machine.getTopWall();
        bottomWallPosition = machine.getBottomWall();
        lengthToGap = machine.getLengthToGap();
        gapWidth = machine.getGapWidth();
        hasHitWall = false;
        
    }

    /**
     * Move this object according to its position and speed and redraw.
     **/
    public void move()
    {
         // remove from universe at the current position
        machine.erase(this);
        
        // compute new position
        currentYLocation += speedYTravel;
        currentXLocation += speedXTravel;
      
    }
    
    /**
     * return the horizontal position of this object
     */
    public int getXPosition()
    {
        return currentXLocation;
    }
    
    /**
     * return the vertical position of this object
     */
    public int getYPosition()
    {
        return currentYLocation;
    }
    
    /**
     * return the radius of this object
     */
    public int getRadius()
    {
        return radius;
    }
    
    /**
     * return the diameter of this object
     */
    public int getDiameter()
    {
        return 2*radius;
    }
    
    /**
     * return the colour of this object
     */
    public Color getColor()
    {
        return colour;
    }
    
    /**
     * Return if the ball has hit a wall
     */
    
    public boolean getHasHitWall()
    {
        return hasHitWall;
    }
    
}
