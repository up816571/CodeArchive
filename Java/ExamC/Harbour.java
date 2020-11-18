import java.util.*;

/**
 * Class to represent a harbour.
 * 
 * @author Claire Ancient
 * @version 2017.02.15
 */
public class Harbour
{
    private ArrayList<Boat> harbour;

    /**
     * Initialisation required for the harbour list
     */
    public Harbour()
    {
        harbour = new ArrayList<Boat>();
        
        dockBoat(new Boat("Cyan", 10, "Southampton", 23));
        dockBoat(new Boat("Octopus", 42, "Liverpool", 56));
        dockBoat(new Boat("Lionheart", 50, "Southampton", 1));
        dockBoat(new Boat("Seven Seas", 10, "Southampton", 16));
        dockBoat(new Boat("Hokulani", 200, "Plymouth", 3));
        dockBoat(new Boat("Baglietto", 10, "Liverpool", 45));
        dockBoat(new Boat("The Maraya", 10, "Southampton", 37));
        dockBoat(new Boat("Serenity", 42, "Plymouth", 81));
        dockBoat(new Boat("Dreamweaver", 42, "Plymouth", 19));
        dockBoat(new Boat("Pegasus", 50, "Liverpool", 67));
        
    }

    /**
     * Store a new boat in the harbour list
     * @param   newBoat     the boat to be stored
     */
    public void dockBoat(Boat newBoat)
    {
        // ****** INSERT CODE HERE ******
    }
    
    /**
     * Counts the number of boats currently docked at the harbour
     * @return      the number of boats in the harbour
     */
    public int countBoats()
    {
        // ****** INSERT CODE HERE ******
        return 0;   //this line only here to allow Harbour to compile, replace with your code
    }
    
    /**
     * Undock a boat from the harbour
     * @param   i   index of the boat to undock
     */
    public void undockBoat(int i)
    {
        // ****** INSERT CODE HERE ******
    }
    
    /**
     * Print the details of boats which have a particular home port
     * @param   reqHomePort     the home port to print the associated boats for
     */
    public void printBoatsWithHomePort(String reqHomePort)
    {
        // ****** INSERT CODE HERE ******
    }
    
    /**
     * Find a particular boat based on the berth number, and print the details
     * @param   searchBerth     the berth for which the boat details are required
     */
    public void findBoat(int searchBerth)
    {
        // ****** INSERT CODE HERE ******        
    }
}
