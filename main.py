import numpy as np
import pygame

tileset = pygame.image.load('tileset.png')

tile_size = 32
tiles = [pygame.transform.scale(tileset.subsurface(pygame.Rect(i * 8, j * 8, 8, 8)), (tile_size, tile_size)) for j in
         range(9) for i in range(40)]

# Create a grid
grid_size = (20, 20)
grid = np.zeros(grid_size, dtype=int)
grid.fill(32)


def draw_grid():
    for y, row in enumerate(grid):
        for x, tile_id in enumerate(row):
            screen.blit(tiles[tile_id], (x * tile_size, y * tile_size))


def draw_sel_grid():
    for y in range(9):
        for x in range(40):
            screen.blit(tiles[x + 40 * y], (x * tile_size, y * tile_size + grid_size[0] * tile_size))


def export_grid():
    with open('output.txt', 'w') as f:
        for row in grid:
            f.write(' '.join(map(str, row)) + '\n')


pygame.init()
screen = pygame.display.set_mode((max(grid_size[1] * tile_size, 40 * 32), grid_size[0] * tile_size + 9 * 32))

clock = pygame.time.Clock()

curTile = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                curTile = (curTile + 1) % 360
            elif event.key == pygame.K_s:
                curTile -= 1
                if curTile < 0:
                    curTile = 359
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                pass

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        curTile = (curTile + 1) % 360
    if keys[pygame.K_w]:
        curTile -= 1
        if curTile < 0:
            curTile = 359

    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        if y < grid_size[0] * tile_size and x < grid_size[1] * tile_size:
            grid[y // tile_size, x // tile_size] = curTile
        else:
            curTile = x // tile_size + 40 * ((y - (grid_size[0] * tile_size)) // tile_size)
            print(curTile)
    if pygame.mouse.get_pressed()[2]:
        x, y = pygame.mouse.get_pos()
        if y < grid_size[0] * tile_size and x < grid_size[1] * tile_size:
            grid[y // tile_size, x // tile_size] = 32

    screen.fill((255, 255, 255))
    draw_grid()
    draw_sel_grid()
    screen.blit(tiles[curTile], (grid_size[1] * tile_size, 0))
    pygame.display.flip()
    clock.tick(60)

export_grid()
pygame.quit()
