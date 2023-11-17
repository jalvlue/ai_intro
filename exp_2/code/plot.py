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
def pathPlot(path):
    x = [city.getX() for city in path]
    y = [city.getY() for city in path]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker="o", linestyle="-", color="blue")

    for _, city in enumerate(path):
        dx = city.getX()
        dy = city.getY()
        plt.text(dx, dy, f"({dx},{dy})", ha="right")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Route Map")
    plt.grid(True)
    plt.show()
