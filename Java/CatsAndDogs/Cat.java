public class Cat
{
    private String name;
    private int age;
    private String furColour;
    private boolean disposition;
    
    public Cat(String catName)
    {
        name = catName;
        age = 1;
        furColour = "ginger";
        disposition = true;
    }
    
    public String getName()
    {
        return name;
    }
    
    public void changeName(String newName)
    {
        name = newName;
    }
    
    public int getAge()
    {
        return age;
    }
    
    public void changeAge(int newAge)
    {
        age = newAge;
    }
    
    public String getFur()
    {
        return furColour;
    }
    
    public void changeFurColour(String newFur)
    {
        furColour = newFur;
    }
    
    public boolean getDisposition() 
    {
        return disposition;
    }
    
    public void changeDisposition(boolean newDis)
    {
        disposition = newDis;
    }
    
    public void purr()
    {
        System.out.println("Purr");
    }
   
    public void miaow()
    {
        System.out.println("miaow");
    }
}
