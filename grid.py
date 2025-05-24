import pygame

ROWS = 40
WIDTH = 800
GAP = WIDTH // ROWS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (64, 224, 208)
PURPLE = (128, 0, 128)
GREY = (200, 200, 200)

class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = row * GAP
        self.y = col * GAP
        self.color = WHITE
        self.neighbors = []

    def get_pos(self):
        return self.row, self.col

    def is_closed(self): return self.color == RED
    def is_open(self): return self.color == GREEN
    def is_barrier(self): return self.color == BLACK
    def is_start(self): return self.color == BLUE
    def is_end(self): return self.color == PURPLE

    def reset(self): self.color = WHITE
    def make_start(self): self.color = BLUE
    def make_closed(self): self.color = RED
    def make_open(self): self.color = GREEN
    def make_barrier(self): self.color = BLACK
    def make_end(self): self.color = PURPLE
    def make_path(self): self.color = GREY

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, GAP, GAP))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < ROWS - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])
        if self.col < ROWS - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])

def make_grid():
    return [[Node(i, j) for j in range(ROWS)] for i in range(ROWS)]

def draw_grid(win):
    for i in range(ROWS):
        pygame.draw.line(win, GREY, (0, i * GAP), (WIDTH, i * GAP))
        for j in range(ROWS):
            pygame.draw.line(win, GREY, (j * GAP, 0), (j * GAP, WIDTH))

def draw(win, grid):
    win.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(win)
    draw_grid(win)
    pygame.display.update()

def get_clicked_pos(pos):
    y, x = pos
    row = y // GAP
    col = x // GAP
    return row, col
