from queue import Queue
import util


def bfs_search(initial_state, goal_state):
    frontier = Queue()
    came_from = dict()

    start_node = util.Node(initial_state)

    frontier.put(start_node)
    came_from[initial_state] = None

    while not frontier.empty():
        current_node = frontier.get()
        current_state = current_node.get_state()

        if current_state == goal_state:
            return came_from

        empty_row, emopty_col = util.find_empty_tile(current_state)

        for new_row, new_col in util.get_possible_actions(empty_row, emopty_col):
            new_state = util.swap_tiles(
                current_state, empty_row, emopty_col, new_row, new_col
            )

            if new_state not in came_from:
                new_node = util.Node(new_state)
                frontier.put(new_node)
                came_from[new_state] = current_node.get_state()

    return None
