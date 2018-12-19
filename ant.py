import math
import random

class Ant:

    def __init__(self, i, aco):
        self.index = i
        self.reset_ant(aco)

    def reset_ant(self, aco):
        self.path_length = 0  # initial ant's path length
        # starting city is indexed at 0
        self.currCity = aco.cities[0]
        # ant's path, each item is (x_cord, y_cord)
        self.path = []
        self.path.append(aco.cities[0])
        # unvisited cities for the current ant
        self.unvisited = []
        self.unvisited.extend(aco.cities[1:])
        # the probability distribution for the next city
        self.transition_probs = []

    # city_y: the next city
    def get_transition_prob(self, aco, city_y):
        b = 0
        a = aco.routing_table[self.currCity.index][city_y.index]
        for c in self.unvisited:
            b = b + aco.routing_table[self.currCity.index][c.index]
        trans_prob = a/float(b)
        return trans_prob

    def euclidean_distance(self, a, b):
        return (math.sqrt(math.pow((a.x - b.x), 2.0) + math.pow((a.y - b.y), 2.0)))

    def calc_path_length(self):
        sum_dist=0.00
        for i in range(0,len(self.path)):
            try:
                eucli_dist =  self.euclidean_distance(self.path[i], self.path[i+1])
                sum_dist += eucli_dist
                self.path_length = sum_dist
            except:
                return sum_dist
