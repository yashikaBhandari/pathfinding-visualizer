from queue import Queue
import heapq

def bfs(draw, grid, start, end):
    queue = Queue()
    queue.put(start)
    came_from = {start: None}

    while not queue.empty():
        current = queue.get()

        if current == end:
            break

        for neighbor in current.neighbors:
            if neighbor not in came_from:
                queue.put(neighbor)
                came_from[neighbor] = current
                neighbor.make_open()
        draw()

        if current != start:
            current.make_closed()

    return reconstruct_path(draw, came_from, end)


def dfs(draw, grid, start, end):
    stack = [start]
    came_from = {start: None}

    while stack:
        current = stack.pop()

        if current == end:
            break

        for neighbor in current.neighbors:
            if neighbor not in came_from:
                stack.append(neighbor)
                came_from[neighbor] = current
                neighbor.make_open()
        draw()

        if current != start:
            current.make_closed()

    return reconstruct_path(draw, came_from, end)


def dijkstra(draw, grid, start, end):
    count = 0
    open_set = []
    heapq.heappush(open_set, (0, count, start))
    came_from = {}
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0

    while open_set:
        _, _, current = heapq.heappop(open_set)

        if current == end:
            break

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                heapq.heappush(open_set, (g_score[neighbor], count, neighbor))
                neighbor.make_open()
                count += 1

        draw()
        if current != start:
            current.make_closed()

    return reconstruct_path(draw, came_from, end)


def reconstruct_path(draw, came_from, current):
    while current in came_from:
        current = came_from[current]
        if current:
            current.make_path()
            draw()
