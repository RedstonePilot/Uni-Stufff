package Geometry;

public class Shape {
    String colour;
    boolean filled;

    public Shape() {
        this.colour = "red";
        this.filled = true;
    }

    public Shape(String colour, boolean filled) {
        this.colour = colour;
        this.filled = filled;

    }

    public boolean isFilled() {
        return this.filled;
    }

    public void setFilled(boolean state) {
        this.filled = state;
    }

    public String getColour() {
        return this.colour;
    }

    public void setColour(String newColour) {
        this.colour = newColour;
    }

    public String toString() {
        if (this.filled) {
            return "A shape with colour: " + this.colour + "and is filled";
        }
        return "A shape with colour: " + this.colour + "and is not filled";
    }

}
