package tools;

public class InvalidOperationException extends Exception {
    public InvalidOperationException() {
        super();
    }

    public InvalidOperationException(String m) {
        super(m);
    }

    public InvalidOperationException(String m, Throwable c) {
        super(m, c);
    }

    public InvalidOperationException(Throwable c) {
        super(c);
    }
}