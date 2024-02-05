# AIM 4 : Write program to implement A* search alogorithm on 15 puzzle problem, with depth of each state

import heapq

def puzzle_heuristic(state, goal_state):
    """
    A simple heuristic function for the 15 Puzzle.
    It calculates the Manhattan distance between each tile in the current state and its goal position.
    """
    total_distance = 0
    for i in range(4):
        for j in range(4):
            if state[i][j] != 0:
                goal_position = divmod(goal_state.index(state[i][j]), 4)
                total_distance += abs(i - goal_position[0]) + abs(j - goal_position[1])
    return total_distance

def is_goal_state(state, goal_state):
    return state == goal_state

def get_neighbors(state):
    neighbors = []
    empty_row, empty_col = find_empty_tile(state)

    # Check and generate neighbors
    for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = empty_row + move[0], empty_col + move[1]
        if 0 <= new_row < 4 and 0 <= new_col < 4:
            new_state = [row[:] for row in state]
            new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
            neighbors.append(new_state)

    return neighbors

def find_empty_tile(state):
    for i in range(4):
        for j in range(4):
            if state[i][j] == 0:
                return i, j

def a_star_search(initial_state, goal_state):
    priority_queue = [(0, initial_state, [])]  # (priority, state, path)
    visited_states = set()

    while priority_queue:
        current_cost, current_state, current_path = heapq.heappop(priority_queue)

        if is_goal_state(current_state, goal_state):
            return current_path, len(current_path)

        if tuple(map(tuple, current_state)) in visited_states:
            continue

        visited_states.add(tuple(map(tuple, current_state)))

        neighbors = get_neighbors(current_state)
        for neighbor in neighbors:
            if tuple(map(tuple, neighbor)) not in visited_states:
                priority = len(current_path) + puzzle_heuristic(neighbor, goal_state)
                heapq.heappush(priority_queue, (priority, neighbor, current_path + [neighbor]))

    return None, None  # No solution found

if __name__ == "__main__":
    initial_state = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ]

    goal_state = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ]

    path, depth = a_star_search(initial_state, goal_state)

    if path is not None:
        print("Solution found!")
        for step, state in enumerate(path):
            print(f"Step {step + 1}:")
            for row in state:
                print(row)
            print()
        print(f"Depth of the solution: {depth}")
    else:
        print("No solution found.")
