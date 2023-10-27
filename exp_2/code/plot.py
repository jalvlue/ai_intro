import enum
import util
import ga
import matplotlib.pyplot as plt


def distanceEvolvePlot(population, popSize, eliteSize, mutationRate, generations):
    pop = util.initialPopulation(popSize, population)
    progress = []
    progress.append(1 / ga.rankRoutes(pop)[0][1])

    for _ in range(0, generations):
        pop = ga.nextGeneration(pop, eliteSize, mutationRate)
        progress.append(1 / ga.rankRoutes(pop)[0][1])

    plt.plot(progress)
    plt.ylabel("Distance")
    plt.xlabel("Generation")
    plt.show()


# TODO: pathPlot()
def pathPlot(bestRoute):
    x_coords = [util.City.x for util.City in bestRoute]
    y_coords = [util.City.y for util.City in bestRoute]

    plt.plot(x_coords, y_coords, "o-")

    for i, city in enumerate(bestRoute):
        plt.annotate(
            str(i + 1),
            (city.x, city.y),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
        )

    plt.xlabel("x")
    plt.ylabel("y")

    plt.show()
