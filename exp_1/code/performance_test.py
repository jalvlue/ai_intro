import util
from bfs import bfs_search
from dfs import dfs_search
import astar
import time
from tqdm import tqdm


def test():
    running_times = list()

    initial_state = util.generate_initial_state()
    goal_state = util.generate_goal_state(initial_state)

    # DFS
    start_time = time.time()
    solution = dfs_search(initial_state, goal_state)
    end_time = time.time()

    if not solution:
        print("Solution not found!")
        return

    dfs_time = end_time - start_time
    running_times.append(dfs_time)

    # BFS
    start_time = time.time()
    solution = bfs_search(initial_state, goal_state)
    end_time = time.time()

    if not solution:
        print("Solution not found!")
        return

    bfs_time = end_time - start_time
    running_times.append(bfs_time)

    # manhattan_heuristic A*
    start_time = time.time()
    solution = astar.a_star_search(initial_state, goal_state, astar.manhattan_heuristic)
    end_time = time.time()

    if not solution:
        print("Solution not found!")
        return

    manhhattan_time = end_time - start_time
    running_times.append(manhhattan_time)

    # misplaced_tiles_heuristic A*
    start_time = time.time()
    solution = astar.a_star_search(
        initial_state, goal_state, astar.misplaced_tiles_heuristic
    )
    end_time = time.time()

    if not solution:
        print("Solution not found!")
        return

    misplaced_time = end_time - start_time
    running_times.append(misplaced_time)

    return running_times


if __name__ == "__main__":
    running_times = [0.0, 0.0, 0.0, 0.0]
    for _ in tqdm(range(10)):
        rt = test()
        if rt:
            running_times = [x + y for x, y in zip(running_times, rt)]

    average_running_time = [x / 10.0 for x in running_times]

    print(
        "average running time of DFS in 10 tests: "
        + str(average_running_time[0])
        + "\n"
    )
    print(
        "average running time of BFS in 10 tests: "
        + str(average_running_time[1])
        + "\n"
    )
    print(
        "average running time of manhattan_heuristic A* in 10 tests: "
        + str(average_running_time[2])
        + "\n"
    )
    print(
        "average running time of misplaced_tiles_heuristic A* in 10 tests: "
        + str(average_running_time[3])
        + "\n"
    )
