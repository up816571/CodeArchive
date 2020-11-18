import java.awt.*;

/**
 * Write a description of class Pinball1 here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */

public class Pinball1 extends PinballObject
{
    private int originRadius;

    public Pinball1(int xPos, int yPos, int xVel, int yVel, Color objectColor, int objectRadius, Machine theMachine)
    {
        super(xPos, yPos, xVel, yVel, objectColor, objectRadius, theMachine);
        originRadius = objectRadius;
    }
    
    public void hitWall()
    {
        int tempRadius;
        if (hasHitWall) 
        {
            tempRadius = (int)(radius / 10);
            radius = radius + tempRadius;
        }
        else
        {
            radius = originRadius;
        }
    }
    
    public void move()
    {
         // remove from universe at the current position
        machine.erase(this);
        
        // compute new position
        currentYLocation += speedYTravel;
        currentXLocation += speedXTravel;
        
        // check if it has hit the leftwall
        if(currentXLocation <= (leftWallPosition + radius)) 
        {
            hitWall();
            currentXLocation = leftWallPosition + radius;
            speedXTravel = -speedXTravel; 
            hasHitWall = !hasHitWall;
        }
        
        // check if it has hit the rightwall
        if(currentXLocation >= (rightWallPosition - radius)) 
        {
            hitWall();
            currentXLocation = rightWallPosition - radius;
            speedXTravel = -speedXTravel; 
            hasHitWall = !hasHitWall;
        }
        
        // check if it has hit the topwall
        if(currentYLocation <= (topWallPosition + radius)) 
        {
            hitWall();
            currentYLocation = topWallPosition + radius;
            speedYTravel = -speedYTravel; 
            hasHitWall = !hasHitWall;
        }
        
        // check if it has hit the bottomwall
        if((currentYLocation >= (bottomWallPosition - radius)) && ((currentXLocation <= (lengthToGap -radius)) || (currentXLocation >= (lengthToGap + (gapWidth * 2) + radius)))) 
        {
             hitWall();
             currentYLocation = bottomWallPosition - radius;
             speedYTravel = -speedYTravel;  
             hasHitWall = !hasHitWall;
        }
        
        if((currentYLocation >= (bottomWallPosition - 10)) && (currentXLocation - radius >= (lengthToGap )) && (currentXLocation + radius <= (lengthToGap + (gapWidth *2) )))
        {
            machine.erase(this);
            machine.setRunning();
        }

        // draw again at new position
        machine.draw(this);
    
    }
    
}
