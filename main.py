import pygame
from pygame.locals import *
import os
import random


WIDTH, HEIGHT = 360, 360
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hide and Seek")

WHITE = (255, 255, 255)

FPS = 60

CHARACTER_WIDTH, CHARACTER_HEIGHT = 16, 16
BACKGROUND_WIDTH, BACKGROUND_HEIGHT = 360, 360
WALL_WIDTH, WALL_HEIGHT = 30, 30

BACKGROUND_IMAGE = pygame.image.load(os.path.join("Assets", "background.png"))
BACKGROUND = pygame.transform.scale(
    BACKGROUND_IMAGE, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT)
)
RED_CHARACTER_IMAGE = pygame.image.load(os.path.join("Assets", "red_character.png"))
RED_CHARACTER = pygame.transform.scale(
    RED_CHARACTER_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT)
)
BLUE_CHARACTER_IMAGE = pygame.image.load(os.path.join("Assets", "blue_character.png"))
BLUE_CHARACTER = pygame.transform.scale(
    BLUE_CHARACTER_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT)
)

WALL_IMAGE = pygame.image.load(os.path.join("Assets", "wall.png"))
WALL = pygame.transform.scale(WALL_IMAGE, (WALL_WIDTH, WALL_HEIGHT))

walls = []


def create_wall(wall):
    WIN.blit(WALL, (wall.x, wall.y))


def create_map():
    WIN.fill(WHITE)
    WIN.blit(BACKGROUND, (0, 0))
    for i in range(random.randint(0, 16)):
        rand_pos_x = random.randrange(0, BACKGROUND_WIDTH, WALL_WIDTH)
        rand_pos_y = random.randrange(0, BACKGROUND_HEIGHT, WALL_HEIGHT)
        for wall in walls:
            while rand_pos_x == wall.x and rand_pos_y == wall.y and i != 16:
                rand_pos_x = random.randrange(0, BACKGROUND_WIDTH, WALL_WIDTH)
                rand_pos_y = random.randrange(0, BACKGROUND_HEIGHT, WALL_HEIGHT)
        wall = pygame.Rect(rand_pos_x, rand_pos_y, WALL_WIDTH, WALL_HEIGHT)
        create_wall(wall)
        walls.append(wall)
        print(rand_pos_x, rand_pos_y)
    pygame.display.update()


def draw_window(red, blue):
    WIN.blit(RED_CHARACTER, (red.x, red.y))
    WIN.blit(BLUE_CHARACTER, (blue.x, blue.y))
    pygame.display.update()


def main():
    create_map()
    red = pygame.Rect(100, 100, CHARACTER_WIDTH, CHARACTER_HEIGHT)
    blue = pygame.Rect(200, 100, CHARACTER_WIDTH, CHARACTER_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window(red, blue)
    pygame.quit()


if __name__ == "__main__":
    main()