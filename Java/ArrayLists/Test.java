import java.util.*;

public class Test
{
    private ArrayList<String> names;
    
    public Test()
    {
        names = new ArrayList<String>();
    }
    
    public void removetest()
    {
        names.add("henlo");
        Iterator<String> it = names.iterator();
        while (it.hasNext()) {
            it.next();
            if (it.equals("henlo")) 
            {
                it.remove();
            }
        }
        names.remove("henlo");
        names.add("hi");
    }
    
    public void removeItem()
    {
        //For loop
        for (String i:names)
        {
            if (i.equals("henlo"))
            {
                names.remove(i);
            }     
        }
    }
    
    public void print()
    {
        for (String i:names)
        {
            System.out.println(i);
        } 
    }
    
    public int HowMany()
    {
        names.contains("hi");
        return names.size();
    }
    
    public void WhileLoop() 
    {
        boolean found = false;
        int index = 0;
        String currentString; 
        
        while(index < names.size() && !found)
        {
            currentString = names.get(index);
            if(names.get(index).equals("hi"))
            {
                System.out.println("Found");
                found = true;
            }
            index ++;
        }
    }  
    
}