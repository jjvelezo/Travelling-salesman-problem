#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <random>
#include <limits>
#include <sstream>
#include <chrono> // Para medir el tiempo

using namespace std;
using namespace chrono;

// Leer las coordenadas desde un archivo
vector<pair<double, double>> readCoordinates(const string& filename) {
    ifstream file(filename);
    vector<pair<double, double>> coordinates;
    double x, y;

    while (file >> x >> y) {
        coordinates.emplace_back(x, y);
    }

    return coordinates;
}

// Leer las distancias desde un archivo
vector<vector<double>> readDistances(const string& filename) {
    ifstream file(filename);
    vector<vector<double>> distances;
    string line;

    while (getline(file, line)) {
        vector<double> row;
        stringstream ss(line);
        double value;
        while (ss >> value) {
            row.push_back(value);
        }
        distances.push_back(row);
    }

    return distances;
}

// Calcular la longitud de una ruta
double calculateRouteLength(const vector<int>& route, const vector<vector<double>>& distances) {
    double length = 0.0;
    for (size_t i = 0; i < route.size() - 1; ++i) {
        length += distances[route[i]][route[i + 1]];
    }
    length += distances[route.back()][route[0]]; 
    return length;
}

// Algoritmo de recocido simulado
pair<vector<int>, double> simulatedAnnealing(const vector<vector<double>>& distances, 
                                             double initialTemperature = 10000.0, 
                                             double coolingRate = 0.99, 
                                             int iterations = 15000) {
    int n = distances.size();
    vector<int> currentRoute(n);
    iota(currentRoute.begin(), currentRoute.end(), 0); 
    shuffle(currentRoute.begin(), currentRoute.end(), default_random_engine(random_device{}()));
    
    vector<int> bestRoute = currentRoute;
    double bestLength = calculateRouteLength(bestRoute, distances);
    double temperature = initialTemperature;

    random_device rd;
    mt19937 gen(rd());
    uniform_real_distribution<> dis(0.0, 1.0);

    while (temperature > 1.0) {
        for (int iter = 0; iter < iterations; ++iter) {
            vector<int> newRoute = currentRoute;
            int i = rand() % n;
            int j = rand() % n;
            if (i > j) swap(i, j);
            reverse(newRoute.begin() + i, newRoute.begin() + j + 1);

            double currentLength = calculateRouteLength(currentRoute, distances);
            double newLength = calculateRouteLength(newRoute, distances);
            double delta = newLength - currentLength;

            if (delta < 0 || dis(gen) < exp(-delta / temperature)) {
                currentRoute = newRoute;
                if (newLength < bestLength) {
                    bestRoute = newRoute;
                    bestLength = newLength;
                }
            }
        }

        temperature *= coolingRate;
    }

    return {bestRoute, bestLength};
}

int main() {
    // Inicio del cronómetro
    auto start = high_resolution_clock::now();

    // Leer coordenadas y distancias
    auto coordinates = readCoordinates("Coord1.txt");
    auto distances = readDistances("Dist1.txt");

    // Ejecutar el algoritmo
    auto [bestRoute, bestLength] = simulatedAnnealing(distances);

    // Fin del cronómetro
    auto end = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(end - start);

    // Mostrar los resultados
    cout << "Best route found with Simulated Annealing: [";
    for (size_t i = 0; i < bestRoute.size(); ++i) {
        cout << bestRoute[i];
        if (i < bestRoute.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
    cout << "Length of the best route (Simulated Annealing): " << bestLength << endl;

    // Mostrar tiempo de ejecución
    cout << "Execution time: " << duration.count() << " ms" << endl;

    return 0;
}
