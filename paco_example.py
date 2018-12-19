import paco
import random
import math
import matplotlib.pyplot as plt

num_cities = 48
# Intialize the ACO algorithm with some parameter values
aco = paco.ACO(num_cities, initial_pheromone=1, alpha=1, beta=3,
            pheromone_deposit=2, evaporation_constant=0.6)

with open("./att48.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

for line in content:
    items = line.split()
    num = int(items[0]) - 1
    x_cord = int(items[1])
    y_cord = int(items[2])
    aco.add_cities(paco.City(num, x_cord, y_cord))

# run the aco algorithm and return the shortest path
ants = 20
shortest_path = aco.get_best_path(num_ants = ants, num_steps = 10)
# print the shortest path length found in the aco
print("Number of ants used: {}".format(ants))
print("Shortest route found: {0:.3f}".format(aco.shortest_path_len))

plt.figure(1, figsize = [12,10], facecolor = '#F0F0F0')
plt.margins(0.1,0.1)

for i,c in enumerate(aco.cities): # output the cities to a plot
    if i == 0:
        plt.title("Visualization of ACO algorithms on TSP (48 cities)")
        plt.ylabel("Y - Coordinates of the cities")
        plt.xlabel("X - Coordinates of the cities")
        plt.plot(c.x, c.y,'gx') # the first city to be printed will be green
    else:
        plt.plot(c.x, c.y,'ro')

for i in range(0,len(shortest_path)-1): # plot connecting lines between each city visited in the order they are visited
    plt.plot([shortest_path[i].x,shortest_path[i+1].x],[shortest_path[i].y,shortest_path[i+1].y],'c-', linewidth=2.0,alpha=0.4)
    plt.pause(0.05)

plt.show()
