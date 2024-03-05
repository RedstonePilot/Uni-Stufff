package sof2week03softwarelab;

import java.util.Arrays;

public class Vector {
    public double[] vector;

    public Vector(double[] args) {
        this.vector = args.clone();

    }

    public String toString() {// java.util.Arrays
        String str = "[";
        for (double element : vector) {
            str = str.concat(String.valueOf(element) + ",");
        }
        str = str.substring(0, str.length() - 1);
        str = str.concat("]");
        return str;
    }

    public int size() {
        return vector.length;
    }

    public double get(int index) {
        return vector[index];
    }

    public double set(int index, double value) {
        double old = get(index);
        vector[index] = value;

        return old;
    }

    public Vector scalarProduct(double scalar) {
        double[] parts = new double[size()];
        for (int i = 0; i < size(); i++) {
            parts[i] = vector[i] * scalar;
        }

        return new Vector(parts);
    }

    public Vector add(Vector other) {
        if (size() != other.size()) {
            return null;
        }
        double[] parts = new double[size()];
        for (int i = 0; i < size(); i++) {
            parts[i] = vector[i] + other.vector[i];
        }
        return new Vector(parts);
    }

    public boolean equals(Object other) {
        if (this == other) {
            return true;
        }
        if (other == null) {
            return false;
        }
        if (getClass() != other.getClass()) {
            return false;
        }
        Vector test = (Vector) other;

        return Arrays.equals(this.vector, test.vector);

    }

    public static void main(String[] args) {
        Vector vect = new Vector(new double[] { 1.0, 2.0, 3.0 });
        System.out.println(vect.toString());
        System.out.println(vect.set(0, 5));
        System.out.println(vect.get(0));
        System.out.println(vect.toString());
        Vector newV = vect.scalarProduct(5);
        System.out.println(newV.toString());
        Vector bigV = vect.add(newV);
        System.out.println(bigV.toString());

    }

}
