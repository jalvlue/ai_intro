from queue import PriorityQueue
import util
from util import n


# heuristic function (Manhattan distance)
def manhattan_heuristic(state, goal_state):
    def get_position(index, state):
        for i in range(n):
            for j in range(n):
                if index == state[i][j]:
                    return (i, j)
        return (-1, -1)

    distance = 0
    for i in range(n):
        for j in range(n):
            tile = state[i][j]
            goal_row, goal_col = get_position(tile, goal_state)
            distance += abs(i - goal_row) + abs(j - goal_col)

    return distance


# heuristic function (misplaced tiles number)
def misplaced_tiles_heuristic(state, goal_state):
    misplaced_count = 0
    for i in range(n):
        for j in range(n):
            if state[i][j] != goal_state[i][j]:
                misplaced_count += 1

    return misplaced_count


class astarNode:
    def __init__(self, initial_state, goal_state, heuristic, cost=0):
        self.state = initial_state
        self.cost = cost
        self.heuristic = heuristic(initial_state, goal_state)
        self.priority = self.cost + self.heuristic

    def __lt__(self, other):
        return self.priority < other.priority

    def get_state(self):
        return self.state

    def get_cost(self):
        return self.cost


def a_star_search(initial_state, goal_state, heuristic):
    frontier = PriorityQueue()

    came_from = dict()

    start_node = astarNode(initial_state, goal_state, heuristic)

    frontier.put(start_node)
    came_from[initial_state] = None

    while not frontier.empty():
        current_node = frontier.get()
        current_state = current_node.get_state()

        if current_state == goal_state:
            return came_from

        empty_row, empty_col = util.find_empty_tile(current_state)

        for new_row, new_col in util.get_possible_actions(empty_row, empty_col):
            new_state = util.swap_tiles(
                current_state,
                empty_row,
                empty_col,
                new_row,
                new_col,
            )

            # utili.print_state(new_state)

            if new_state not in came_from:
                new_node = astarNode(
                    new_state,
                    goal_state,
                    heuristic,
                    current_node.get_cost() + 1,
                )
                frontier.put(new_node)
                came_from[new_state] = current_node.get_state()

    return None
