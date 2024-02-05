# AIM 3 : Write program to implement A* search alogorithm

import heapq

def heuristic(state):
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    heuristic_cost = 0
    for i in range(len(state)):
        if state[i] != goal[i]:
            heuristic_cost += 1
    return heuristic_cost

def a_star(start, goal):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, (0, start))
    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            return True
        closed_list.add(current)
        for neighbor in get_neighbors(current):
            if neighbor not in closed_list:
                g_cost = current[1]
                h_cost = heuristic(neighbor)
                f_cost = g_cost + h_cost
                heapq.heappush(open_list, (f_cost, neighbor))
    return False

def get_neighbors(state):
    neighbors = []
    empty_index = state.index(0)
    row, col = empty_index // 3, empty_index % 3
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for direction in directions:
        new_row, new_col = row + direction[0], col + direction[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = list(state)
            new_state[empty_index], new_state[new_row * 3 + new_col] = new_state[new_row * 3 + new_col], new_state[empty_index]
            neighbors.append((new_state, 1))  # 1 is the cost of moving
    return neighbors

start = [1, 2, 3, 4, 5, 6, 7, 8, 0]
goal = [2, 1, 3, 4, 6, 7, 0, 5, 8]
print(a_star(start, goal))