
import tools.InvalidOperationException;
import tools.TallyCounter;

public class MainApp {

    public static void main(String[] args) {
        TallyCounter tallyCount = new TallyCounter();
        System.out.println(tallyCount);
        try {
            tallyCount.increment();
        } catch (InvalidOperationException e) {
            System.out.println("Too big");

        } finally {
            System.out.println("What goes here???");
        }

        System.out.println(tallyCount.read());
        tallyCount.reset();
        System.out.println(tallyCount.toString());
    }

}
