import java.io.*;
import java.util.*;

public class SimulatedAnnealing {

    public static double[][] readCoordinates(String filename) throws IOException {
        List<double[]> coordinates = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] parts = line.trim().split("\\s+");
                double x = Double.parseDouble(parts[0]);
                double y = Double.parseDouble(parts[1]);
                coordinates.add(new double[]{x, y});
            }
        }
        return coordinates.toArray(new double[0][]);
    }


    public static double[][] readDistances(String filename) throws IOException {
        List<double[]> distances = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] parts = line.trim().split("\\s+");
                double[] row = Arrays.stream(parts).mapToDouble(Double::parseDouble).toArray();
                distances.add(row);
            }
        }
        return distances.toArray(new double[0][]);
    }


    public static double calculateRouteLength(int[] route, double[][] distances) {
        double length = 0.0;
        for (int i = 0; i < route.length - 1; i++) {
            length += distances[route[i]][route[i + 1]];
        }
        length += distances[route[route.length - 1]][route[0]]; 
        return length;
    }


    public static int[] simulatedAnnealing(double[][] distances, double initialTemperature, double coolingRate, int iterations) {
        int n = distances.length;
        int[] currentRoute = new int[n];
        for (int i = 0; i < n; i++) {
            currentRoute[i] = i;
        }
        shuffleArray(currentRoute);

        int[] bestRoute = currentRoute.clone();
        double bestLength = calculateRouteLength(bestRoute, distances);

        double temperature = initialTemperature;

        while (temperature > 1) {
            for (int i = 0; i < iterations; i++) {
                int[] newRoute = currentRoute.clone();
                int index1 = (int) (Math.random() * n);
                int index2 = (int) (Math.random() * n);
                reverseSubarray(newRoute, Math.min(index1, index2), Math.max(index1, index2));

                double newLength = calculateRouteLength(newRoute, distances);
                double delta = newLength - calculateRouteLength(currentRoute, distances);

                if (delta < 0 || Math.random() < Math.exp(-delta / temperature)) {
                    currentRoute = newRoute;
                    if (newLength < bestLength) {
                        bestRoute = newRoute.clone();
                        bestLength = newLength;
                    }
                }
            }
            temperature *= coolingRate;
        }
        System.out.println("Best Route Length: " + bestLength);
        return bestRoute;
    }


    public static void shuffleArray(int[] array) {
        Random random = new Random();
        for (int i = array.length - 1; i > 0; i--) {
            int index = random.nextInt(i + 1);
            int temp = array[index];
            array[index] = array[i];
            array[i] = temp;
        }
    }

 
    public static void reverseSubarray(int[] array, int start, int end) {
        while (start < end) {
            int temp = array[start];
            array[start] = array[end];
            array[end] = temp;
            start++;
            end--;
        }
    }


    public static void main(String[] args) {
        try {
            double[][] distances = readDistances("Dist1.txt");

            long startTime = System.nanoTime();

            int[] bestRoute = simulatedAnnealing(distances, 10000, 0.999, 12000);

            long endTime = System.nanoTime();

            double elapsedTimeInSeconds = (endTime - startTime) / 1_000_000_000.0;

            System.out.println("Best route found:");
            for (int city : bestRoute) {
                System.out.print(city + " ");
            }
            System.out.println("\nExecution time: " + elapsedTimeInSeconds + " seconds");

        } catch (IOException e) {
            System.err.println("Error reading files: " + e.getMessage());
        }
    }
}
