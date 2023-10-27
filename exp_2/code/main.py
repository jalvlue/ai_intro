import util
import ga
import random
import plot


def main():
    # Create list of cities
    N = int(input("Enter number of cities: "))
    cityList = []
    for _ in range(0, N):
        cityList.append(
            util.City(x=int(random.random() * 200), y=int(random.random() * 200))
        )

    path = ga.geneticAlgorithm(
        cityList,
        100,
        20,
        0.1,
        500,
    )

    plot.distanceEvolvePlot(cityList, 100, 20, 0.01, 300)

    plot.pathPlot(path)


if __name__ == "__main__":
    main()
