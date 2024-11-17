import matplotlib.pyplot as plt


def read_coordinates(file_name):
    coordinates = []
    with open(file_name, 'r') as file:
        for line in file:
            x, y = map(float, line.split())
            coordinates.append((x, y))
    return coordinates


def plot_route(coordinates, route):
    x_vals = [coordinates[i][0] for i in route]
    y_vals = [coordinates[i][1] for i in route]
    
    x_vals.append(x_vals[0])
    y_vals.append(y_vals[0])
    
    plt.plot(x_vals, y_vals, marker='o', color='b', linestyle='-', markersize=5)
    
    for i, (x, y) in enumerate(coordinates):
        plt.text(x, y, str(i), fontsize=12, ha='right')
    
    plt.title("Traveling Salesman Route")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.grid()
    plt.show()

route = []

coordinates = read_coordinates('Coord2.txt')
plot_route(coordinates, route)
