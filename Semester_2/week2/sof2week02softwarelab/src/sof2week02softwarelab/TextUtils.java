package sof2week02softwarelab;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.Collectors;

public class TextUtils {

    public static int toBase10(String binary) {
        int output = 0;
        int factor = 1;
        binary = new StringBuilder(binary).reverse().toString();

        for (char c : binary.toCharArray()) {
            int b = (int) c - 48;
            if (b == 1) {
                output = output + factor;
            }
            factor = factor * 2;
        }

        return output;

    }

    public static String[] split(String text) {
        System.out.println(text);
        ArrayList<String> output = new ArrayList<String>();
        ArrayList<Character> tmp = new ArrayList<Character>();

        for (char c : text.toCharArray()) {
            if (c == ' ') {
                String joined = tmp.stream().map(String::valueOf).collect(Collectors.joining());
                output.add(joined);
                tmp.clear();
            } else {
                tmp.add(c);
            }

        }
        String joined = tmp.stream().map(String::valueOf).collect(Collectors.joining());
        output.add(joined);

        String[] result = output.toArray(new String[0]);
        return result;
    }

    public static String[] split(String text, String seperators) {
        System.out.println(text + seperators);
        ArrayList<String> output = new ArrayList<String>();
        ArrayList<Character> tmp = new ArrayList<Character>();

        for (char c : text.toCharArray()) {
            if (seperators.contains(Character.toString(c))) {
                String joined = tmp.stream().map(String::valueOf).collect(Collectors.joining());
                output.add(joined);
                tmp.clear();
            } else {
                tmp.add(c);
            }

        }
        String joined = tmp.stream().map(String::valueOf).collect(Collectors.joining());
        output.add(joined);

        String[] result = output.toArray(new String[0]);
        System.out.println(Arrays.toString(result));
        return result;

    }

    public static int[][] rasterise(int[] data, int width) {
        int[] tmp = new int[width];
        int[][] output = new int[data.length / width][];
        if (data.length % width != 0) {
            return null;
        }

        for (int n = 0; n < data.length; n++) {
            tmp[n % width] = data[n];
            if (n % width == 0) {
                output[n / width] = tmp;
                tmp = new int[width];
            }

        }
        for (int[] row : output) {
            for (int num : row) {
                System.out.print(num + " ");
            }
            System.out.println();
        }

        // Using Arrays.deepToString
        System.out.println(Arrays.deepToString(output));
        return output;
    }

    public static void main(String[] args) {
        // System.out.println(toBase10("10001011"));
        // System.out.println(split("A scratch Your arm s off").length);
        // System.out.println(split("Tis but a scratch.", "?."));
        System.out.println(rasterise(new int[] { 1, 2, 3, 4, 5, 6 }, 2));
    }

}
