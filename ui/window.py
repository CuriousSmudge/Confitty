import pygame as pg
from ..processing import terminal
import inputbox
import button

WIDTH = 360
HEIGHT = 480
FPS = 30

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pg and create window
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Confitty")
clock = pg.time.Clock()  # For syncing the FPS


# Game loop
running = True
while running:
    # 1 Process input/events
    clock.tick(FPS)  # will make the loop run at the same speed all the time
    for event in (
        pg.event.get()
    ):  # gets all the events which have occured till now and keeps tab of them.
        # listening for the the X button at the top
        if event.type == pg.QUIT:
            running = False

    # 3 Draw/render
    screen.fill(BLACK)

    # Done after drawing everything to the screen
    pg.display.flip()

pg.quit()
