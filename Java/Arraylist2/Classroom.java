import java.util.*;

public class Classroom 
{
    
    private ArrayList<Student> students;
    Student varName = new Student("Josh");
    
    public Classroom()
    {
        students = new ArrayList<Student>();
    }
    
    public void addStudent(Student student)
    {
        students.add(student);
    }
    
    
    public void nameSearch(String name)
    {
        students.add(varName);
        for(Student student : students) 
        {
            if (student.getname().equals(name))
            {
                System.out.println("here");
            }
        }
    }
}