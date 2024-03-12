package Geometry;

public class Square extends Rectangle {

    public Square(double sideLength) {
        super(sideLength, sideLength);
    }

    public Square(String colour, boolean filled, double sideLength) {
        super(colour, filled, sideLength, sideLength);
    }

    public double getSide() {
        return this.width;
    }

    public void setSide(double newSide) {
        this.width = newSide;
        this.length = newSide;
    }

    @Override
    public void setWidth(double newWidth) {
        this.width = newWidth;
        super.setLength(newWidth);
    }

    @Override
    public void setLength(double newLength) {
        this.length = newLength;
        super.setWidth(newLength);
    }

    @Override
    public String toString() {
        return "A Square with side= " + this.width + ", which is a subclass of " + super.toString();
    }

    public static void main(String[] args) {
        Square sq = new Square("green", true, 5.5);

        System.out.println(sq.toString());
    }
}
