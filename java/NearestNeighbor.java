import java.io.*;
import java.util.*;

public class NearestNeighbor {


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


    public static double calculateDistance(double[] point1, double[] point2) {
        return Math.sqrt(Math.pow(point1[0] - point2[0], 2) + Math.pow(point1[1] - point2[1], 2));
    }

  
    public static int[] nearestNeighbor(double[][] coordinates) {
        int n = coordinates.length;
        boolean[] visited = new boolean[n];
        List<Integer> route = new ArrayList<>();
        route.add(0);
        visited[0] = true;

        while (route.size() < n) {
            int lastCity = route.get(route.size() - 1);
            int nearestCity = -1;
            double smallestDistance = Double.MAX_VALUE;

            for (int i = 0; i < n; i++) {
                if (!visited[i]) {
                    double dist = calculateDistance(coordinates[lastCity], coordinates[i]);
                    if (dist < smallestDistance) {
                        smallestDistance = dist;
                        nearestCity = i;
                    }
                }
            }

            route.add(nearestCity);
            visited[nearestCity] = true;
        }

        return route.stream().mapToInt(i -> i).toArray();
    }

 
    public static double calculateRouteLength(int[] route, double[][] coordinates) {
        double length = 0.0;
        for (int i = 0; i < route.length - 1; i++) {
            length += calculateDistance(coordinates[route[i]], coordinates[route[i + 1]]);
        }
        length += calculateDistance(coordinates[route[route.length - 1]], coordinates[route[0]]);
        return length;
    }

    public static void main(String[] args) {
        try {

            double[][] coordinates = readCoordinates("Coord1.txt");

            int[] route = nearestNeighbor(coordinates);
            double routeLength = calculateRouteLength(route, coordinates);


            System.out.println("Route with the Nearest Neighbor algorithm: " + Arrays.toString(route));
            System.out.println("Length of the route (Nearest Neighbor): " + routeLength);

        } catch (IOException e) {
            System.err.println("Error reading the file: " + e.getMessage());
        }
    }
}
