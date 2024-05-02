import numpy as np
import pygame

# Get the tile you will use to create the menu
tileset = pygame.image.load('tileset/tileset.png')
tile_size = 32 # The square size of the tile or sprite

tiles = [pygame.transform.scale(tileset.subsurface(pygame.Rect(i * 8, j * 8, 8, 8)), (tile_size, tile_size)) for j in
         range(9) for i in range(40)]

# Grid where the value od the sprites where be saved
grid_size = (20, 25)
gridSprValues = np.zeros(grid_size, dtype=int)
gridSprValues.fill(32)


def draw_grid(gridExport: np.ndarray):
    """
    Draw the inputted matrix of values on the screen
    :param gridExport: The grid containing the matrix with the values of the sprites you want to draw
    :return:
    """
    for y, row in enumerate(gridExport):
        for x, tile_id in enumerate(row):
            screen.blit(tiles[tile_id], (x * tile_size, y * tile_size))


def draw_sel_grid():
    """
    This function will draw at the bottom of the screen the possible tiles or sprites that you can use
    :return:
    """
    for y in range(9):
        for x in range(40):
            screen.blit(tiles[x + 40 * y], (x * tile_size, y * tile_size + grid_size[0] * tile_size))


def export_grid(outFile: str, gridExport: np.ndarray):
    """
    Export the grid containing the values of the sprites into a file
    :param outFile: The path of the output where the file will be exported
    :param gridExport: The grid which will be exported
    :return:
    """
    with open(outFile, 'w') as f:
        for row in gridExport:
            f.write(' '.join(map(str, row)) + '\n')


# Start values of Pygame
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
        # Check if you pressed inside the canvas or in the sprite selection bellow
        if y < grid_size[0] * tile_size and x < grid_size[1] * tile_size:
            # Paint the sprites in the canvas
            gridSprValues[y // tile_size, x // tile_size] = curTile
        else:
            # Select the new sprite to paint
            curTile = x // tile_size + 40 * ((y - (grid_size[0] * tile_size)) // tile_size)
            print(curTile)
    if pygame.mouse.get_pressed()[2]:
        x, y = pygame.mouse.get_pos()
        if y < grid_size[0] * tile_size and x < grid_size[1] * tile_size:
            gridSprValues[y // tile_size, x // tile_size] = 32

    # Refill and draw the screen
    screen.fill((255, 255, 255))
    draw_grid(gridSprValues)
    draw_sel_grid()
    screen.blit(tiles[curTile], (grid_size[1] * tile_size, 0))

    pygame.display.flip()
    clock.tick(60)

# Export the grid and save it into a file
export_grid("output.txt", gridSprValues)
pygame.quit()
