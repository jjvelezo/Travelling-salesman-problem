import numpy as np
import math


def read_coordinates(filename):
    with open(filename, 'r') as file:
        coordinates = []
        for line in file:
            x, y = map(float, line.strip().split())
            coordinates.append((x, y))
    return np.array(coordinates)


def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def nearest_neighbor(coordinates):
    n = len(coordinates)
    visited = [False] * n
    route = [0]  
    visited[0] = True
    
    while len(route) < n:
        last_city = route[-1]
        nearest_city = None
        smallest_distance = float('inf')
        

        for i in range(n):
            if not visited[i]:
                dist = distance(coordinates[last_city], coordinates[i])
                if dist < smallest_distance:
                    smallest_distance = dist
                    nearest_city = i
        

        route.append(nearest_city)
        visited[nearest_city] = True
    
    return route


def calculate_route_length(route, coordinates):
    length = sum(distance(coordinates[route[i]], coordinates[route[i + 1]]) for i in range(len(route) - 1))
    length += distance(coordinates[route[-1]], coordinates[route[0]]) 
    return length


coordinates = read_coordinates("Coord2.txt")


nearest_neighbor_route = nearest_neighbor(coordinates)
nearest_neighbor_length = calculate_route_length(nearest_neighbor_route, coordinates)


print("Route with the Nearest Neighbor algorithm:", nearest_neighbor_route)
print("Length of the route (Nearest Neighbor):", nearest_neighbor_length)


