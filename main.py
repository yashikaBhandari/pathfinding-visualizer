import pygame
from grid import make_grid, draw, get_clicked_pos
from algorithms import bfs, dfs, dijkstra

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Graph Pathfinding Visualizer - Dijkstra, BFS, DFS")

def main(win):
    grid = make_grid()
    start = None
    end = None
    run = True

    while run:
        draw(win, grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # Left click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos)
                node = grid[row][col]
                if not start:
                    start = node
                    start.make_start()
                elif not end and node != start:
                    end = node
                    end.make_end()
                elif node != start and node != end:
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]:  # Right click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    bfs(lambda: draw(win, grid), grid, start, end)

                if event.key == pygame.K_d and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    dfs(lambda: draw(win, grid), grid, start, end)

                if event.key == pygame.K_k and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    dijkstra(lambda: draw(win, grid), grid, start, end)

                if event.key == pygame.K_r:
                    start = None
                    end = None
                    grid = make_grid()

    pygame.quit()

main(WIN)
