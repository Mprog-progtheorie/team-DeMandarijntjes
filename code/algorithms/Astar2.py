from queue import PriorityQueue
import numpy as np

def heuristic(current, goal):
    h = abs(np.array(current) - np.array(goal))
    return h.sum()

def gate_neighbours(current, grid, path):
    neighbours = list()
    moves = list()
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(8):
                moves.append((x, y, z))

    for i in moves:
        neighbour = tuple(np.array(current) + np.array(i))
        if neighbour not in path:
            if neighbour in grid:
                if grid.get(neighbour)[0]:
                    neighbours.append(neighbour)

    return neighbours


def neighbours(current, grid, path):
    neighbours = list()

    # kan in for loop
    moves = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    for i in moves:
        neighbour = tuple(np.array(current) + np.array(i))
        if neighbour not in path:
            if neighbour in grid:
                if grid.get(neighbour)[0]:
                    neighbours.append(neighbour)

    return neighbours

def a_star(start, end, grid, ceiling_count):
    pq = PriorityQueue()
    
    path = [start]
    if heuristic(start, end) < 5:
        for i in range(ceiling_count):
            force_up = list(path[-1])
            force_up[2] = i
            force_up = tuple(force_up)
            if grid.get(force_up)[0]:
                path.append(force_up)
            else:
                neighbour_list = neighbours(path[-1], grid, path)
                if neighbour_list:
                    for neighbour in neighbour_list:
                        path.append(neighbour)
                        break
                else:
                    break
        
    f = grid.get(path[-1])[1] + heuristic(path[-1], end)

    visited = set()

    pq.put((f, path))

    while not pq.empty():
        path = pq.get()[1]
        current = path[-1]
        if current == end:
            return path

        for i in neighbours(current, grid, path):
            new_path = path + [i]
            g = len(new_path) + grid.get(i)[1]
            f = g + heuristic(i, end)
            if i not in visited:
                pq.put((f, new_path))
                visited.add(i)

    return False

def a_star_basic(start, end, grid):
    pq = PriorityQueue()
    
    path = [start]
        
    f = grid.get(path[-1])[1] + heuristic(path[-1], end)

    visited = set()

    pq.put((f, path))

    while not pq.empty():
        path = pq.get()[1]
        current = path[-1]
        if current == end:
            return path

        for i in neighbours(current, grid, path):
            new_path = path + [i]
            f = len(new_path) + heuristic(i, end)
            if i not in visited:
                pq.put((f, new_path))
                visited.add(i)

    return False

def make_grid(gates):
    if len(gates) == 25:
        y_range = 13
    else:
        y_range = 17

    grid = {}
    for x in range(18):
        for y in range(y_range):
            for z in range(8):
                g = 8 - z
                grid[(x, y, z)] = [True, (g * 2)]
     
    return grid
