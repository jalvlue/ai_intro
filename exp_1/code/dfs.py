from collections import deque
import util


def dfs_search(initial_state, goal_state):
    stack = deque()
    came_from = dict()

    start_node = util.Node(initial_state)

    stack.append(start_node)
    came_from[initial_state] = None

    while stack:
        current_node = stack.pop()
        current_state = current_node.get_state()

        if current_state == goal_state:
            return came_from

        empty_row, empty_col = util.find_empty_tile(current_state)
        for new_row, new_col in util.get_possible_actions(empty_row, empty_col):
            new_state = util.swap_tiles(
                current_state, empty_row, empty_col, new_row, new_col
            )

            if new_state not in came_from:
                new_node = util.Node(new_state)
                stack.append(new_node)
                came_from[new_state] = current_state

    return None
