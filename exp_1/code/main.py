import astar
import util
import bfs
import dfs


def main():
    initial_state = util.generate_initial_state()
    goal_state = util.generate_goal_state(initial_state)

    # DFS
    print("====================================")
    print("DFS:")

    solution = dfs.dfs_search(initial_state, goal_state)

    if solution:
        print("Solution found,\nMoves:")
        util.trace(solution, goal_state)
    else:
        print("No solution found.")

    # BFS
    print("====================================")
    print("BFS:")

    solution = bfs.bfs_search(initial_state, goal_state)

    if solution:
        print("Solution found,\nMoves:")
        util.trace(solution, goal_state)
    else:
        print("No solution found.")

    # manhattan_heuristic A*
    print("====================================")
    print("A* with manhattan_heuristic:")

    solution = astar.a_star_search(initial_state, goal_state, astar.manhattan_heuristic)

    if solution:
        print("Solution found,\nMoves:")
        util.trace(solution, goal_state)
    else:
        print("No solution found.")

    # misplaced_tiles_heuristic A*
    print("====================================")
    print("A* with misplaced_tiles_heuristic:")

    solution = astar.a_star_search(
        initial_state, goal_state, astar.misplaced_tiles_heuristic
    )

    if solution:
        print("Solution found!\nMoves:")
        util.trace(solution, goal_state)
    else:
        print("No solution found.")

    print("\nInitial state:")
    util.print_state(initial_state)

    print("\nGoal state:")
    util.print_state(goal_state)


if __name__ == "__main__":
    main()
