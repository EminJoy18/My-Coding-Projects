import javax.swing.*;
public class GUI 
{
    public static void main(String[] args) {
        JFrame frame=new JFrame("Click Me");
        JButton button=new JButton("CLICK ME");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add(button);
        frame.setSize(1920,480);
        frame.setVisible(true);
    }
    
}
