public class Student 
{
    private String name;
    private String id;
    private int credits;
    private String favourite;
    
    public Student(String studentName, String studentID,String favouriteSubject)
    {
        name = studentName;
        id = studentID;
        credits = 0;
        favourite = favouriteSubject;
    }
    
    public String getSubject()
    {
        return favourite;
    }
    
    public void changeFavourite(String replacementFavourite)
    {
        favourite = replacementFavourite;
    }
    
    public String getName()
    {
        return name;
    }
    
    public void changeName(String replacementName)
    {
        name = replacementName;
    }
    
    public String getStudentID()
    {
        return id;
    }
    
    public int getCredits()
    {
        return credits;
    }
    
    public void addCredits(int additionalPoints)
    {
        credits += additionalPoints;
    }
    
    public String getLoginName()
    {
        return "UP" + id;
    }
    
    public void hasStudentPassed()
    {
        if (credits >= 120)
            System.out.println("Passed");
        else
            System.out.println("Failed");
     }
    
    public void print()
    {
        System.out.println(name + ", student ID: " + id + ", credits: " + credits + ", Favourite subject :" +favourite);
    }
}

