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
    x = [coord[0] for coord in path]
    y = [coord[1] for coord in path]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker="o", linestyle="-", color="blue")

    for _, coord in enumerate(path):
        plt.text(coord[0], coord[1], f"({coord[0]},{coord[1]})", ha="right")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Route Map")
    plt.grid(True)
    plt.show()


route = [
    (147, 19),
    (162, 65),
    (153, 80),
    (163, 109),
    (182, 128),
    (181, 187),
    (132, 177),
    (124, 167),
    (112, 156),
    (93, 155),
    (104, 196),
    (64, 189),
    (70, 153),
    (11, 143),
    (1, 127),
    (52, 109),
    (62, 116),
    (59, 77),
    (60, 50),
    (8, 47),
    (3, 16),
    (8, 16),
    (22, 36),
    (50, 35),
    (94, 32),
]

pathPlot(route)
