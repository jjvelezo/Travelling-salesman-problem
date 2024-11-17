import numpy as np
import math
import random
import matplotlib.pyplot as plt

def read_coordinates(filename):
    with open(filename, 'r') as file:
        coordinates = []
        for line in file:
            x, y = map(float, line.strip().split())
            coordinates.append((x, y))
    return np.array(coordinates)

def read_distances(filename):
    with open(filename, 'r') as file:
        distances = [list(map(float, line.strip().split())) for line in file]
    return np.array(distances)

def calculate_route_length(route, distances):
    length = sum(distances[route[i], route[i + 1]] for i in range(len(route) - 1))
    length += distances[route[-1], route[0]]  # close the loop
    return length

def simulated_annealing(distances, initial_temperature=10000, cooling_rate=0.99, iterations=900):
    n = len(distances)
    current_route = list(range(n))
    random.shuffle(current_route)
    best_route = current_route[:]
    best_length = calculate_route_length(best_route, distances)
    
    temperature = initial_temperature
    
    while temperature > 1:
        for _ in range(iterations):
            new_route = current_route[:]
            i, j = sorted(random.sample(range(n), 2))
            new_route[i:j+1] = reversed(new_route[i:j+1])
            
            new_length = calculate_route_length(new_route, distances)
            
            delta = new_length - calculate_route_length(current_route, distances)
            if delta < 0 or random.random() < math.exp(-delta / temperature):
                current_route = new_route[:]
                
                if new_length < best_length:
                    best_route = new_route[:]
                    best_length = new_length
        
        temperature *= cooling_rate
    
    return best_route, best_length

def plot_route(coordinates, route, title="TSP Solution"):
    plt.figure(figsize=(10, 6))
    
    for i in range(len(route) - 1):
        plt.plot([coordinates[route[i]][0], coordinates[route[i + 1]][0]],
                 [coordinates[route[i]][1], coordinates[route[i + 1]][1]], 'b-', alpha=0.7)
    plt.plot([coordinates[route[-1]][0], coordinates[route[0]][0]],
             [coordinates[route[-1]][1], coordinates[route[0]][1]], 'b-', alpha=0.7)
    
    plt.plot(coordinates[:, 0], coordinates[:, 1], 'ro', markersize=5)
    
    for i, (x, y) in enumerate(coordinates):
        plt.text(x, y, str(i), fontsize=12, ha='right')
    
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

# Load coordinates and distances from files
coordinates = read_coordinates("Coord3.txt")
distances = read_distances("Dist3.txt")

# Run the Simulated Annealing algorithm
best_route, best_length = simulated_annealing(distances)
print("Best route found with Simulated Annealing:", best_route)
print("Length of the best route (Simulated Annealing):", best_length)

# Call plot_route to visualize the solution of Simulated Annealing
plot_route(coordinates, best_route, title="TSP Solution with Simulated Annealing")
