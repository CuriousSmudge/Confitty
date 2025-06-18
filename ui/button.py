import pyray as pr
from ui import con
from dataclasses import dataclass


class Button:
    mousePos = pr.get_mouse_position()

    def __init__(self, rect: tuple, text, color=con.MANTLE, text_col=con.MAUVE):
        # pr.Rectangle = (x, y, width, height)
        self.rect = rect
        self.text = text
        self.colour = color
        self.textColour = text_col

    def render_button(self):
        # Renders the button to the screen based on the rect
        pr.draw_rectangle_rounded(self.rect, 4, 1, self.colour)
        pr.draw_text(self.text, self.rect[0]+24, self.rect[1]+12, 16, self.textColour)

    def is_clicked(self, mousePos):
        # Checks if the button is currently being clicked
        if pr.check_collision_circle_rec(mousePos, 0.1, self.rect) and pr.is_mouse_button_pressed(pr.MOUSE_BUTTON_LEFT):
            print("Settings Menu Clicked")
            return True
        else:
            return False