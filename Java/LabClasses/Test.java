public class Test
{
    
    public void studentTest()
    {
        Student student1;
        student1 = new Student("Bob","123456");
        
        System.out.println("Name Before: " + student1.getName());
        student1.changeName("Alice");
        System.out.println("Name After: " + student1.getName());
        
        System.out.println("Student ID: " + student1.getStudentID());
        
        System.out.println("Credits Before: " + student1.getCredits());
        student1.addCredits(20);
        System.out.println("Credits After: " + student1.getCredits());
        
        System.out.println(student1.getLoginName());
        student1.print();
    }
}
