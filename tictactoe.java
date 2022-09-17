import java.util.Scanner;

class tictactoe
{
    public static void main(String args[])
    {
        try(Scanner sc=new Scanner(System.in))
        {
        System.out.println("Welcome to TIC-TAC-TOE\n");
        String s1,s2;int r,c;char m[][]=new char[3][3];
        System.out.print("Enter name of Player1: ");
        s1=sc.nextLine();
        System.out.print("Enter name of Player2: ");
        s2=sc.nextLine();System.out.println("\n");
        System.out.println(s1+" you play with 'X' and "+s2+" you play with 'O'\n");
        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
            {
                System.out.print(i+""+j+" || ");
            }
            System.out.println("\n");
        }
        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
            {
                m[i][j]='_';
            }
        }
        System.out.println("Let's Play \n");
        for(int i=0;i<9;i++)
        {
            if(i==0||i%2==0) //asking for output
            {
                System.out.println(s1);
                System.out.println("Enter the row and column: ");
                r=sc.nextInt();c=sc.nextInt();
                    m[r][c]='X';
                for(int k=0;k<3;k++) //displaying the result
                {
                    for(int l=0;l<3;l++)
                    {
                        System.out.print(m[k][l]+" ");
                    }
                    System.out.println();
                }
                System.out.println();
                if(Character.compare(m[0][0],m[0][1])==0&&Character.compare(m[0][2],m[0][1])==0&&Character.compare(m[0][0],'X')==0||Character.compare(m[1][0],m[1][1])==0&&Character.compare(m[1][2],m[1][1])==0&&Character.compare(m[1][0],'X')==0||Character.compare(m[2][0],m[2][1])==0&&Character.compare(m[2][0],m[2][2])==0&&Character.compare(m[2][0],'X')==0||Character.compare(m[0][0],m[1][0])==0&&Character.compare(m[0][0],m[2][0])==0&&Character.compare(m[0][0],'X')==0||Character.compare(m[0][1],m[1][1])==0&&Character.compare(m[0][1],m[2][1])==0&Character.compare('X',m[0][1])==0||Character.compare(m[0][2],m[1][2])==0&&Character.compare(m[0][2],m[2][2])==0&&Character.compare('X',m[0][2])==0||Character.compare(m[0][0],m[1][1])==0&&Character.compare(m[0][0],m[2][2])==0&&Character.compare(m[0][0],'X')==0||Character.compare(m[0][2],m[1][1])==0&&Character.compare(m[2][0],m[1][1])==0&&Character.compare(m[0][2],'X')==0)
                {
                    System.out.println(s1+" WINS!!");
                    System.out.println("CONGRATULATIONS");
                    break;
                }
                else
                System.out.println("It's a TIE!");
            }
            else
            {
                System.out.println(s2);
                System.out.println("Enter the row and column: ");
                r=sc.nextInt();c=sc.nextInt();  //make it such that once written cant be overwritten
                    m[r][c]='O';
                for(int k=0;k<3;k++) //displaying the result
                {
                    for(int l=0;l<3;l++)
                    {
                        System.out.print(m[k][l]+" ");
                    }
                    System.out.println();
                }
                System.out.println();
                if(Character.compare(m[0][0],m[0][1])==0&&Character.compare(m[0][2],m[0][1])==0&&Character.compare(m[0][0],'O')==0||Character.compare(m[1][0],m[1][1])==0&&Character.compare(m[1][2],m[1][1])==0&&Character.compare(m[1][0],'O')==0||Character.compare(m[2][0],m[2][1])==0&&Character.compare(m[2][0],m[2][2])==0&&Character.compare(m[2][0],'O')==0||Character.compare(m[0][0],m[1][0])==0&&Character.compare(m[0][0],m[2][0])==0&&Character.compare(m[0][0],'O')==0||Character.compare(m[0][1],m[1][1])==0&&Character.compare(m[0][1],m[2][1])==0&Character.compare('O',m[0][1])==0||Character.compare(m[0][2],m[1][2])==0&&Character.compare(m[0][2],m[2][2])==0&&Character.compare('O',m[0][2])==0||Character.compare(m[0][0],m[1][1])==0&&Character.compare(m[0][0],m[2][2])==0&&Character.compare(m[0][0],'O')==0||Character.compare(m[0][2],m[1][1])==0&&Character.compare(m[2][0],m[1][1])==0&&Character.compare(m[0][2],'O')==0)
                {
                    System.out.println(s2+" WINS!!");
                    System.out.println("CONGRATULATIONS");
                    break;
                }
                else
                System.out.println("It's a TIE!");
            }
        }
    }
    }
}