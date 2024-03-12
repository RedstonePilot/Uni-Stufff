package Geometry;

public class Circle extends Shape {
    double radius;

    public Circle() {
        this.radius = 1.0;
    }

    public Circle(String colour, boolean filled, double radius) {
        super(colour, filled);
        this.radius = radius;

    }

    public double getRadius() {
        return this.radius;
    }

    public void setRadius(double newRadius) {
        this.radius = newRadius;
    }

    public double getArea() {
        return Math.PI * Math.pow(this.radius, 2);
    }

    public double getPerimeter() {
        return Math.PI * 2 * this.radius;
    }

    @Override
    public String toString() {
        return "A Circle with radius: " + this.radius + ", which is a subclass of " + super.toString();
    }
}
