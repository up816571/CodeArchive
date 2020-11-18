
/**
 * Class to represent a docked boat.
 * 
 * THIS CLASS MUST NOT BE CHANGED
 * 
 * @author Claire Ancient 
 * @version 2017.02.15
 */
public class Boat
{
    private String boatName;
    private int engineHP;
    private String homePort;
    private int dockedBerthNo;

    /**
     * Constructor for objects of class Boat
     */
    public Boat(String btName, int btEngine, String btHome, int btBerth)
    {
        boatName = btName;
        engineHP = btEngine;
        homePort = btHome;
        dockedBerthNo = btBerth;
    }

    /**
     * Method to get the name of the boat
     */
    public String getBoatName()
    {
        return boatName;
    }
    
    /**
     * Method to get the engine size of the boat
     */
    public int getEngineSize()
    {
        return engineHP;
    }
    
    /**
     * Method to get the home port of the boat
     */
    public String getHomePort()
    {
        return homePort;
    }
    
    /**
     * Method to get the berth number of where boat is docked
     */
    public int getBerthNo()
    {
        return dockedBerthNo;
    }
    
    /**
     * Method to print the details of the boat
     */
    public void printBoatDetails()
    {
        System.out.println("Boat Name: " + boatName);
        System.out.println("Boat Engine Size: " + engineHP + "hp");
        System.out.println("Boat Home Port: " + homePort);
        System.out.println("Current Berth Number: " + dockedBerthNo);
    }
}
