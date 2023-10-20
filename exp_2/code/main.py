import util
import ga
import random


def main():
    # Create list of cities
    N = int(input("Enter number of cities: "))
    cityList = []
    for _ in range(0, N):
        cityList.append(
            util.City(x=int(random.random() * 200), y=int(random.random() * 200))
        )

    ga.geneticAlgorithm(
        cityList,
        100,
        20,
        0.01,
        500,
    )


if __name__ == "__main__":
    main()
