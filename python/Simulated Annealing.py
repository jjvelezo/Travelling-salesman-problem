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
    length += distances[route[-1], route[0]]
    return length

def simulated_annealing(distances, initial_temperature=10000, cooling_rate=0.99, iterations=1100):
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



coordinates = read_coordinates("Coord1.txt")
distances = read_distances("Dist1.txt")


best_route, best_length = simulated_annealing(distances)
print("Best route found with Simulated Annealing:", best_route)
print("Length of the best route (Simulated Annealing):", best_length)
