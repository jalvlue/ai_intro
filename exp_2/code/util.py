import numpy as np
import random


class City:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def distance(self, city):
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        distance = np.sqrt((xDis**2) + (yDis**2))
        return distance

    def __repr__(self) -> str:
        return "(" + str(self.x) + "," + str(self.y) + ")"


class Fitness:
    def __init__(self, route) -> None:
        self.route = route
        self.distance = 0
        self.finness = 0.0

    def routeDistance(self):
        if self.distance == 0:
            pathDistance = 0
            for i in range(len(self.route)):
                fromCity = self.route[i]
                toCity = None
                if i + 1 < len(self.route):
                    toCity = self.route[i + 1]
                else:
                    toCity = self.route[0]
                pathDistance += fromCity.distance(toCity)
            self.distance = pathDistance

        return self.distance

    def routeFitness(self):
        if self.finness == 0:
            self.fitness = 1 / float(self.routeDistance())

        return self.fitness


def createCityList():
    N = int(input("Enter number of cities: "))
    cityList = []

    for _ in range(0, N):
        cityList.append(
            City(x=int(random.random() * 200), y=int(random.random() * 200))
        )

    return cityList


def createRoute(cityList):
    route = random.sample(cityList, len(cityList))

    return route


"""
@param popSize: population size
@param cityList: list of cities
"""


def initialPopulation(popSize, cityList):
    population = []

    for _ in range(0, popSize):
        population.append(createRoute(cityList))

    return population
