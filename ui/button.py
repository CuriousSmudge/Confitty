import pyray as pr
from ui import con
from dataclasses import dataclass


# self.width = con.WIDTH // self.character_size[0]
# self.height = con.HEIGHT // self.character_size[1]

class Button:
    mousePos = pr.get_mouse_position()

    def __init__(self, rect: tuple, text, color=con.MANTLE, text_col=con.MAUVE):
        # pr.Rectangle = (x, y, width, height)
        self.rect = rect
        self.text = text
        self.colour = color
        self.textColour = text_col

    def render_button(self):
        pr.draw_rectangle_rounded(self.rect, 4, 1, self.colour)
        pr.draw_text(self.text, self.rect[0]+24, self.rect[1]+12, 16, self.textColour)

    def is_clicked(self, mousePos):
        if pr.check_collision_circle_rec(mousePos, 0.1, self.rect) and pr.is_mouse_button_pressed(pr.MOUSE_BUTTON_LEFT):
            print("Settings Menu Clicked")
            # self.colour = con.CRUST
            return True
        else:
            return False



# TODO
# - [ ] Button takes in callback
# - [ ] Button should have update method for each frame
# - [ ]
# - [ ]
# - [ ]

# # import pygame as pg
# from ui import window

# # Colours
# BUTTON = (24, 24, 37)
# BUTTON_CLICK = (17, 17, 27)
# TEXT = (203, 166, 247)


# class Button:
#     mousePos = pg.mouse.get_pos()

#     def __init__(self, shape: pg.Rect, text: str):
#         self.shape = shape
#         self.text = text
#         # self.textSize =
#         self.colour = BUTTON
#         self.click = BUTTON_CLICK
#         self.textColour = TEXT
#         self.fontObject = pg.font.Font()
#         self.fontObject.align = pg.FONT_CENTER

#     def is_clicked(self, mousePos) -> bool:
#         if pg.mouse.get_just_released()[0] and self.shape.collidepoint(mousePos):
#             print("Button clicked!")
#             return True
#         else:
#             return False

#     def render_button(self):
#         pg.draw.rect(screen, self.colour, self.shape)
#         textSurface = self.render_text()
#         textX = self.shape.width // 2 + self.shape.x - textSurface.width // 2
#         textY = self.shape.height // 2 + self.shape.y - textSurface.height // 2
#         screen.blit(textSurface, (textX, textY))

#     def render_text(self):
#         textSurface = self.fontObject.render(self.text, True, TEXT)
#         return textSurface
