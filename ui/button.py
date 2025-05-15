import pygame as pg
from ui import window

# Colours
BUTTON = (24, 24, 37)
BUTTON_CLICK = (17, 17, 27)
TEXT = (203, 166, 247)


class Button:
    mousePos = pg.mouse.get_pos()

    def __init__(self, shape: pg.Rect, text: str):
        self.shape = shape
        self.text = text
        # self.textSize =
        self.colour = BUTTON
        self.click = BUTTON_CLICK
        self.textColour = TEXT
        self.fontObject = pg.font.Font()
        self.fontObject.align = pg.FONT_CENTER

    def is_clicked(self, mousePos) -> bool:
        if pg.mouse.get_just_released()[0] and self.shape.collidepoint(mousePos):
            print("Button clicked!")
            return True
        else:
            return False

    def render_button(self):
        pg.draw.rect(screen, self.colour, self.shape)
        textSurface = self.render_text()
        textX = self.shape.width // 2 + self.shape.x - textSurface.width // 2
        textY = self.shape.height // 2 + self.shape.y - textSurface.height // 2
        screen.blit(textSurface, (textX, textY))

    def render_text(self):
        textSurface = self.fontObject.render(self.text, True, TEXT)
        return textSurface
