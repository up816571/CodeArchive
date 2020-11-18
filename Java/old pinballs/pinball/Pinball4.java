import java.awt.*;

/**
 * Write a description of class Pinball4 here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */

public class Pinball4 extends PinballObject
{
    /**
     * Constructor for objects of class Pinball4
     */
    private Color[] allowedColours = {Color.CYAN, Color.YELLOW, Color.MAGENTA};
    private Color currentColour;
    
    
    public Pinball4(int xPos, int yPos, int xVel, int yVel, Color objectColor, int objectRadius, Machine theMachine)
    {
        super(xPos, yPos, xVel, yVel, objectColor, objectRadius, theMachine);
        theMachine.getPinballs().add(this);
    }
    
    public void hitWall()
    {
        currentColour = colour;
        if (currentColour == Color.CYAN)
        {
            colour = allowedColours[1];
        }
        else if (currentColour == Color.YELLOW)
        {
            colour = allowedColours[2];
        }
        else 
        {
            colour = allowedColours[0];
        }
    }
    
    public void move()
    {
        super.move();
        
        for (PinballObject pinballs : machine.getPinballs())
        {
            double difference;
            int a = currentXLocation - pinballs.getXPosition();
            int b = currentYLocation - pinballs.getYPosition(); 
            difference = Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2));
            if(difference <= radius + pinballs.getRadius() && pinballs !=this)
            {
                speedXTravel = - speedXTravel;
                speedYTravel = - speedYTravel; 
            }
        }
        
        // check if it has hit the leftwall
        if(currentXLocation <= (leftWallPosition + radius)) 
        {
            hitWall();
            currentXLocation = leftWallPosition + radius;
            speedXTravel = -speedXTravel; 
        }
        
        // check if it has hit the rightwall
        if(currentXLocation >= (rightWallPosition - radius)) 
        {
            hitWall();
            currentXLocation = rightWallPosition - radius;
            speedXTravel = -speedXTravel; 
        }
        
        // check if it has hit the topwall
        if(currentYLocation <= (topWallPosition + radius)) 
        {
            hitWall();
            currentYLocation = topWallPosition + radius;
            speedYTravel = -speedYTravel; 
        }
        
        // check if it has hit the bottomwall
        if (currentYLocation >= bottomWallPosition - radius)
        {
        //If it is in the gap and small enough to fit end the simulation else bounce off
            if(currentXLocation - radius >= lengthToGap && currentXLocation + radius <= lengthToGap + gapWidth * 2 && radius * 2 <= gapWidth)
            {
                machine.erase(this);
                machine.setRunning();
            }
            else
            {
                hitWall();
                currentYLocation = bottomWallPosition - radius;
                speedYTravel = -speedYTravel;  
            } 
        }
        
        for (Bumper bumper : machine.getBumps())
        {
            double difference;
            int a = currentXLocation - bumper.getXPosition();
            int b = currentYLocation - bumper.getYPosition(); 
            difference = Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2));
            if(difference < radius + bumper.getRadius())
            {
                speedXTravel = -speedXTravel;
                speedYTravel = -speedYTravel; 
            }
        }
        
        // draw again at new position
        machine.draw(this);
    
    }

}
