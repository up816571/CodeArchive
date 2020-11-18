import java.awt.*;
import java.util.*;

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
        theMachine.getPinballs().add(this);
    }
    
    public void hitWall()
    {
        int tempRadius;
        if (hasHitWall) 
        {
            tempRadius = (int)(radius / 10);
            radius += tempRadius;
        }
        else
        {
            radius = originRadius;
        }
    }
    
    public void move()
    {    
        super.move();
        
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
                hasHitWall = !hasHitWall;
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
