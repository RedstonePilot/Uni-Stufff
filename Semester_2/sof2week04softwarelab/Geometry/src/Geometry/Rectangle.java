package Geometry;

public class Rectangle extends Shape {

    double width;
    double length;

    public Rectangle() {
        this.width = 1.0;
        this.length = 1.0;
    }

    public Rectangle(double width, double length) {
        this.width = width;
        this.length = length;

    }

    public Rectangle(String colour, boolean filled, double width, double length) {

        super(colour, filled);
        this.width = width;
        this.length = length;
    }

    public double getLength() {
        return this.length;
    }

    public double getWidth() {
        return this.width;
    }

    public void setLength(double newLength) {
        this.length = newLength;
    }

    public void setWidth(double newWidth) {
        this.width = newWidth;
    }

    public double getArea() {
        return this.length * this.width;
    }

    public double getPerimeter() {
        return this.length * 2 + this.width * 2;
    }

    @Override
    public String toString() {
        return "A Rectangle with width= " + this.width + "and length= " + this.length + ", which is a subclass of"
                + super.toString();
    }
}
