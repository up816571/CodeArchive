public class MailClient
{
    private MailServer server;
    private String user;
    
    public MailClient(MailServer mailServer, String userName)
    {
        server = mailServer;
        user = userName;
    }
    
    public void printNextMailItem()
    {
        MailItem item = server.getNextMailItem(user);
        if(item == null) {
            System.out.println("no new mail.");
        }
        else {
            item.printInfo();
        }
    }
    
    public void sendMailItem(String to, String subject, String message)
    {
        MailItem item = new MailItem(user , to, subject, message);
        server.post(item);
    }
}
            