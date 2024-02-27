package Semester_2.week1;

import java.util.Scanner;

public class HeartRate {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        System.out.print("Enter your age: ");
        int age = keyboard.nextInt();
        System.out.print("Enter your heart rate: ");
        int rate = keyboard.nextInt();

        double maxRate = 208 - 0.7*age;

        if (rate >= 0.9*maxRate) {
            System.out.println("Interval Training");
            
        } else if (rate >= 0.7*maxRate) {
            System.out.println("Threshold Traning");
        } else if (rate >= 0.5*maxRate){
            System.out.println("Aerobatic Training");
        }else{
            System.out.println("Couch Potat");
        }
        keyboard.close();
    }
    
}
