import random

# 3*3 map
n = 3


class Node:
    def __init__(self, initial_state):
        self.state = initial_state

    def get_state(self):
        return self.state


# convert a list of lists into a tuple of tuples
def tuple_state(state: list[list[int]]):
    return tuple(tuple(row) for row in state)


def generate_initial_state():
    numbers = list(range(9))
    random.shuffle(numbers)
    state = [numbers[i : i + n] for i in range(0, n * n, n)]

    return tuple_state(state)


# check if a state is solvable
def is_solvable(initial_state, goal_state):
    def count_inversions(state):
        inversions = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] > state[j] and state[i] != 0 and state[j] != 0:
                    inversions += 1
        return inversions

    flat_initial = [num for row in initial_state for num in row]
    flat_goal = [num for row in goal_state for num in row]

    # make sure all 9 digits are different
    for i in range(len(flat_goal)):
        if flat_initial[i] == flat_goal[i]:
            return False

    inversions_initial = count_inversions(flat_initial)
    inversions_goal = count_inversions(flat_goal)

    return inversions_initial % 2 == inversions_goal % 2


# generate a solvable goal state based on the initial state
def generate_goal_state(initial_state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    numbers = [num for row in initial_state for num in row if num != 0]
    random.shuffle(numbers)
    numbers.append(0)
    goal_state = [numbers[i : i + n] for i in range(0, n * n, n)]
    while not is_solvable(initial_state, goal_state):
        random.shuffle(numbers)
        goal_state = [numbers[i : i + n] for i in range(0, n * n, n)]

    return tuple_state(goal_state)


def trace(came_from, goal_state):
    current_state = goal_state
    path = []
    while current_state != None:
        path.append(current_state)
        current_state = came_from[current_state]
    path.reverse()

    count = 0
    for state in path:
        print("move_" + str(count) + ":")
        count += 1
        print_state(state)
        print("")

    return None


def print_state(state):
    for row in state:
        print(row)

    return None


def find_empty_tile(state):
    for i in range(n):
        for j in range(n):
            if state[i][j] == 0:
                return i, j

    return (0, 0)


def get_possible_actions(row, col):
    actions = []
    if row > 0:
        actions.append((row - 1, col))
    if row < 2:
        actions.append((row + 1, col))
    if col > 0:
        actions.append((row, col - 1))
    if col < 2:
        actions.append((row, col + 1))
    return actions


def swap_tiles(state, row1, col1, row2, col2):
    new_state = list(list(row) for row in state)
    new_state[row1][col1], new_state[row2][col2] = (
        new_state[row2][col2],
        new_state[row1][col1],
    )

    return tuple_state(new_state)
