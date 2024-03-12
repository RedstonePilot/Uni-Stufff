package tools;

public class TallyCounter {
    private int counter;
    private int maxValue;

    public TallyCounter() {
        counter = 0;
        maxValue = 999;
    }

    public TallyCounter(int max) {
        counter = 0;
        maxValue = max;
    }

    public String toString() {
        int padl = Integer.toString(maxValue).length();
        String formatter = "%0" + padl + "d";
        return String.format(formatter, counter);
    }

    public void increment() throws InvalidOperationException {
        if (counter == maxValue) {
            throw new InvalidOperationException("Whooops! Max value reached!");
        } else {
            counter++;
        }
    }

    public void decrement() throws InvalidOperationException {
        if (counter == 0) {
            throw new InvalidOperationException("Oh no the number is too small");
        } else {
            counter--;
        }
    }

    public int read() {
        return counter;
    }

    public void reset() {
        counter = 0;
    }
}
