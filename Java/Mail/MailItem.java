public class MailItem
{
    private String to;
    private String from;
    private String subject;
    private String message;
    private boolean priority;
    
    public MailItem(String setTo, String setFrom, String setSub, String setMes)
    {
        to = setTo;
        from = setFrom;
        subject = setSub;
        message = setMes;
        priority = false;
    }
    
    public String getTo()
    {
        return to;
    }
    
    public String getFrom()
    {
        return from;
    }
    
    public String getSubject()
    {
        return subject;
    }
    
    public String getMessage()
    {
        return message;
    }
    
    public void printInfo()
    {
        System.out.println("To " + to);
        System.out.println("From " + from);
        System.out.println("subject " + subject);
        System.out.println("message " + message);
        if (priority == true) {
            System.out.println("Urgent");
        }
        else {
            System.out.println("Non-Urgent");
        }
    }
}
