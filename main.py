import math
import random

import pygame

pygame.init()

FPS = 60
WIDTH, HEIGHT = 800, 800
# WIDTH, HEIGHT = 1920, 1080
ROWS = COLS = 4

RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS

OUTLINE_COLOR = (187, 173, 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192, 180)
FONT_COLOR = (119, 110, 101)

FONT = pygame.font.SysFont("comicsans", 60, bold=True)
MOVE_VEL = 20

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")


class Tile:
    COLORS = [
        (237, 229, 218),
        (238, 225, 201),
        (243, 178, 122),
        (246, 150, 101),
        (247, 124, 95),
        (247, 95, 59),
        (237, 208, 115),
        (237, 204, 99),
        (236, 202, 80),
    ]

    def __init__(self, value, row, col) -> None:
        self.value = value
        self.row = row
        self.col = col
        self.x = col * RECT_WIDTH
        self.y = row * RECT_HEIGHT

    def get_color(self) -> tuple:
        color_index = int(math.log2(self.value)) - 1
        return self.COLORS[color_index]

    def draw(self, window) -> None:
        color = self.get_color()
        pygame.draw.rect(window, color, (self.x, self.y, RECT_WIDTH, RECT_HEIGHT))
        text = FONT.render(str(self.value), True, FONT_COLOR)
        window.blit(
            text,
            (
                self.x + RECT_WIDTH / 2 - text.get_width() / 2,
                self.y + RECT_HEIGHT / 2 - text.get_height() / 2,
            ),
        )

    def set_pos(self):
        pass

    def move(self, delta) -> None:
        self.row = row
        self.col = col
        self.x = col * RECT_WIDTH
        self.y = row * RECT_HEIGHT


def draw_grid(window) -> None:
    for row in range(1, ROWS):
        y = row * RECT_HEIGHT
        pygame.draw.line(window, OUTLINE_COLOR, (0, y), (WIDTH, y), OUTLINE_THICKNESS)
    for col in range(1, COLS):
        x = col * RECT_HEIGHT
        pygame.draw.line(window, OUTLINE_COLOR, (x, 0), (x, HEIGHT), OUTLINE_THICKNESS)
    pygame.draw.rect(window, OUTLINE_COLOR, (0, 0, WIDTH, HEIGHT), OUTLINE_THICKNESS)


def draw(window, tiles) -> None:
    window.fill(BACKGROUND_COLOR)

    for tile in tiles.values():
        tile.draw(window)

    draw_grid(window)

    pygame.display.update()


def get_random_pos(tiles) -> tuple:
    row = col = None
    while True:
        col = random.randrange(0, COLS)
        row = random.randrange(0, ROWS)
        if f"{row}{col}" not in tiles:
            break
    return row, col


def generate_tiles() -> dict:
    tiles = {}
    for _ in range(2):
        row, col = get_random_pos(tiles)
        tiles[f"{row}{col}"] = Tile(2, row, col)

    return tiles


def main(window) -> None:
    clock = pygame.time.Clock()
    run = True

    tiles = generate_tiles()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(window, tiles)

    pygame.quit()


if __name__ == "__main__":
    main(WINDOW)
