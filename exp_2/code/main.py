import util
import ga
import random
import plot


def main():
    cityList = util.createCityList()

    path = ga.geneticAlgorithm(
        population=cityList,
        popSize=100,
        eliteSize=20,
        mutationRate=0.01,
        generations=500,
    )

    plot.distanceEvolvePlot(
        population=cityList,
        popSize=100,
        eliteSize=20,
        mutationRate=0.01,
        generations=500,
    )

    plot.pathPlot(path)


if __name__ == "__main__":
    main()
