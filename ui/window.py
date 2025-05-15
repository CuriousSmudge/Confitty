import pygame as pg
import os
from processing.terminal import terminal

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 360
HEIGHT = 480


class Window:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Confitty")

        self.clock = pg.time.Clock()
        self.term = terminal.Terminal()

        self.font = pg.font.Font(None, 18)
        self.line_height = self.font.get_linesize()
        self.lines = ['']

    def run(self):
        running = True