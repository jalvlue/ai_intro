import util
import operator
import random
import numpy as np
import pandas as pd

"""
@returns: sorted dict of tuples (index, fitness)
"""


def rankRoutes(population):
    fitnessResults = {}
    for i in range(0, len(population)):
        fitnessResults[i] = util.Fitness(population[i]).routeFitness()

    return sorted(fitnessResults.items(), key=operator.itemgetter(1), reverse=True)


"""
@param popRanked: sorted dict of tuples (index, fitness)
@param eliteSize: number of elite individuals
@returns: list of indices of selected individuals
"""


def selection(popRanked, eliteSize):
    selectionResults = []
    df = pd.DataFrame(np.array(popRanked), columns=["Index", "Fitness"])
    df["cum_sum"] = df.Fitness.cumsum()
    df["cum_perc"] = 100 * df.cum_sum / df.Fitness.sum()

    for i in range(0, eliteSize):
        selectionResults.append(popRanked[i][0])
    for i in range(0, len(popRanked) - eliteSize):
        pick = 100 * random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i, 3]:
                selectionResults.append(popRanked[i][0])
                break

    return selectionResults


"""
@returns: list of selected individuals
"""


def matingPool(population, selectionResults):
    matingpool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingpool.append(population[index])

    return matingpool


def breed(parent_1, parent_2):
    child = []
    childP1 = []
    childP2 = []

    geneA = int(random.random() * len(parent_1))
    geneB = int(random.random() * len(parent_1))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent_1[i])

    childP2 = [item for item in parent_2 if item not in childP1]

    child = childP1 + childP2
    return child


"""
@param eliteSize: number of the best performing individuals,
                  will automatically carry over to the next generation
"""


def breedPopulation(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0, eliteSize):
        children.append(matingpool[i])

    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool) - i - 1])
        children.append(child)

    return children


def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if random.random() < mutationRate:
            swapWith = int(random.random() * len(individual))

            city1 = individual[swapped]
            city2 = individual[swapWith]

            individual[swapped] = city2
            individual[swapWith] = city1

    return individual


def mutatePopulation(population, mutationRate):
    mutatedPop = []

    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)

    return mutatedPop


def nextGeneration(currentGeneration, eliteSize, mutationRate):
    popRanked = rankRoutes(currentGeneration)

    selectionResults = selection(popRanked, eliteSize)

    matingpool = matingPool(currentGeneration, selectionResults)

    children = breedPopulation(matingpool, eliteSize)

    nextGeneration = mutatePopulation(children, mutationRate)

    return nextGeneration


def geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations):
    pop = util.initialPopulation(popSize, population)
    print("Initial distance: " + str(1 / rankRoutes(pop)[0][1]))

    for _ in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)

    print("Final distance: " + str(1 / rankRoutes(pop)[0][1]))
    bestRouteIndex = rankRoutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex]

    return bestRoute
