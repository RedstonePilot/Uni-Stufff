package Semester_2.week1;

import java.util.Scanner;

public class UserInputs {
    public static void main(String[] args) {
        
        Scanner keyboard = new Scanner(System.in);
        System.out.print("Enter an int: ");
        int number = keyboard.nextInt();

        System.out.println("Number entered was: "
                                    + number);
        keyboard.close();
    }
    
}
