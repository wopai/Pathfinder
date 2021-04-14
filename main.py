import pygame
from pygame.locals import *
import os
import random
import math

WIDTH, HEIGHT = 360, 360
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pathfinder")

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

BLUE_CHARACTER_SPAWN_COORDINATES = (100, 100)
RED_CHARACTER_SPAWN_COORDINATES = (200, 200)


def create_wall(wall):
    WIN.blit(WALL, (wall.x, wall.y))


def create_map():
    WIN.fill(WHITE)
    WIN.blit(BACKGROUND, (0, 0)),
    for i in range(random.randint(0, 16)):
        character_colliding = True
        while character_colliding:
            rand_pos_x = random.randrange(0, BACKGROUND_WIDTH, WALL_WIDTH)
            rand_pos_y = random.randrange(0, BACKGROUND_HEIGHT, WALL_HEIGHT)
            # print((rand_pos_x == BLUE_CHARACTER_SPAWN_COORDINATES[0] -
            #        BLUE_CHARACTER_SPAWN_COORDINATES[0] % WALL_WIDTH)
            #       or (rand_pos_x == (BLUE_CHARACTER_SPAWN_COORDINATES[0] + CHARACTER_WIDTH) -
            #           BLUE_CHARACTER_SPAWN_COORDINATES[
            #               0] + CHARACTER_WIDTH % WALL_WIDTH))
            character_colliding = (((rand_pos_x == BLUE_CHARACTER_SPAWN_COORDINATES[0] -
                                     BLUE_CHARACTER_SPAWN_COORDINATES[0] % WALL_WIDTH)
                                    or (rand_pos_x == (BLUE_CHARACTER_SPAWN_COORDINATES[0] + CHARACTER_WIDTH) -
                                        ((BLUE_CHARACTER_SPAWN_COORDINATES[
                                              0] + CHARACTER_WIDTH) % WALL_WIDTH)))
                                   and ((rand_pos_y == BLUE_CHARACTER_SPAWN_COORDINATES[1] -
                                         BLUE_CHARACTER_SPAWN_COORDINATES[1] % WALL_HEIGHT)
                                        or (rand_pos_y == (BLUE_CHARACTER_SPAWN_COORDINATES[1] + CHARACTER_HEIGHT) -
                                            ((BLUE_CHARACTER_SPAWN_COORDINATES[
                                                  1] + CHARACTER_HEIGHT) % WALL_HEIGHT)))) or (
                                          ((rand_pos_x == RED_CHARACTER_SPAWN_COORDINATES[0] -
                                            RED_CHARACTER_SPAWN_COORDINATES[0] % WALL_WIDTH)
                                           or (rand_pos_x == (RED_CHARACTER_SPAWN_COORDINATES[
                                                                  0] + CHARACTER_WIDTH) -
                                               ((RED_CHARACTER_SPAWN_COORDINATES[
                                                     0] + CHARACTER_WIDTH) % WALL_WIDTH))) and (
                                                  (rand_pos_y ==
                                                   RED_CHARACTER_SPAWN_COORDINATES[1] -
                                                   RED_CHARACTER_SPAWN_COORDINATES[
                                                       1] % WALL_HEIGHT)
                                                  or (rand_pos_y ==
                                                      (RED_CHARACTER_SPAWN_COORDINATES[
                                                           1] + CHARACTER_HEIGHT) -
                                                      ((RED_CHARACTER_SPAWN_COORDINATES[
                                                            1] + CHARACTER_HEIGHT) % WALL_HEIGHT))))
            for wall in walls:
                while rand_pos_x == wall.x and rand_pos_y == wall.y:
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


def game_over():
    print("game over...")
    quit()


def check_distance(red, blue):
    """returns left,top,realdist"""
    LEFT, TOP = red.left - blue.left, red.top - blue.top
    realdist = math.sqrt(abs(LEFT) ** 2 + abs(TOP) ** 2)
    if realdist <= math.sqrt(red.width ** 2 + red.height ** 2):
        game_over()
    return LEFT, TOP, realdist


def main():
    create_map()
    red = pygame.Rect(BLUE_CHARACTER_SPAWN_COORDINATES[0], BLUE_CHARACTER_SPAWN_COORDINATES[1],
                      CHARACTER_WIDTH, CHARACTER_HEIGHT)
    blue = pygame.Rect(RED_CHARACTER_SPAWN_COORDINATES[0], RED_CHARACTER_SPAWN_COORDINATES[1],
                       CHARACTER_WIDTH, CHARACTER_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window(red, blue)
        check_distance(red, blue)
    pygame.quit()


if __name__ == "__main__":
    main()
