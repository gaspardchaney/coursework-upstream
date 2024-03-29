"""
CMSC 14200, Spring 2024
Homework #2

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""
import os
import sys
from typing import Optional

import pygame
import pygame.gfxdraw
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

BUTTON_RADIUS = 24
FONT_SIZE = 36

def distance(p1: tuple[int, int], p2: tuple[int, int]) -> float:
    """
    Calculate the distance between two points.

    Input:
        p1 (tuple[int, int]): first point
        p2 (tuple[int, int]): second point

    Returns (float): The distance between p1 and p2.
    """
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

class Incrementer:
    """
    Class for a GUI which displays a number and has buttons to increment
    and decrement the number. 
    """

    width:   int
    height:  int
    border:  int
    number:  int
    buttons: dict[str, tuple[int, int]]

    surface: pygame.surface.Surface
    clock:   pygame.time.Clock
    font:    pygame.font.Font

    def __init__(self, width: int=600, height: int=400, border: int=32):
        """
        Constructor.

        Input:
            width  (int): width of the window
            height (int): height of the window
            border (int): number of pixels in the border around elements
        """
        self.width = width
        self.height = height
        self.border = border
        self.number = 1

        horizontal = self.width - self.border - BUTTON_RADIUS
        vertical = self.height//2
        self.buttons = {"increment": (horizontal, vertical - BUTTON_RADIUS),
                        "decrement": (horizontal, vertical + BUTTON_RADIUS)}

        # initialize Pygame
        pygame.init()
        pygame.display.set_caption("Incrementer")
        self.font = pygame.font.Font(None, size=FONT_SIZE)
        self.surface = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        self.event_loop()

    def _draw_button(self, center: tuple[int, int], label: str,
                           highlight: bool) -> None:
        """
        Draw a button.

        Input:
            center (Tuple[int, int]): center of the button
            label (str): label for button
            highlight (bool): whether or not the button is selected

        Returns (None): Nothing, draws.
        """
        x, y = center

        if highlight:
            pygame.gfxdraw.filled_circle(self.surface, x, y, BUTTON_RADIUS,
                (255, 255, 0))
        else:
            pygame.gfxdraw.filled_circle(self.surface, x, y, BUTTON_RADIUS,
                (255, 255, 255))

        pygame.gfxdraw.aacircle(self.surface, x, y, BUTTON_RADIUS, (0, 0, 0))

        label_img = self.font.render(label, True, (0, 0, 0))
        text_topleft = (x - label_img.get_width() // 2,
                        y - label_img.get_height() // 2)
        self.surface.blit(label_img, text_topleft)

    def _draw_number(self) -> None:
        """
        Draw the number.

        Returns (None): Nothing, draws.
        """
        x, y = self.width//2, self.height//2

        font = pygame.font.Font(None, FONT_SIZE)
        text = font.render(str(self.number), True, (0, 0, 0))
        self.surface.blit(text, (x, y))

    def draw_window(self) -> None:
        """
        Draw the window.

        Returns (None): Nothing, draws.
        """
        incr = False
        decr = False

        self.surface.fill((255, 0, 0))
        self._draw_button(self.buttons["increment"], "+1", incr)
        self._draw_button(self.buttons["decrement"], "-1", decr)
        self._draw_number()

    def event_loop(self) -> None:
        """
        Handle user interaction.

        Returns (None): Nothing.
        """
        while True:
            # process Pygame events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # update the display
            self.draw_window()
            pygame.display.update()
            self.clock.tick(24)

if __name__ == "__main__":
    Incrementer()
