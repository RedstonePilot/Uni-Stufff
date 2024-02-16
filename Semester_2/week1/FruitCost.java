package Semester_2.week1;

import java.util.Scanner;

public class FruitCost {

    public static void main(String[] args) {
    

        Scanner keyboard = new Scanner(System.in);
        System.out.print("Enter the weight of bananas in kg: ");
        double weight = keyboard.nextInt();

        double bananaCost = weight * 3;
        if (bananaCost > 50) {
            bananaCost = bananaCost - 1.5;
            
        }

        bananaCost = bananaCost + 4.99;

        System.out.println("£" + bananaCost);

        
        keyboard.close();
    }
    
}
