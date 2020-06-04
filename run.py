import pygame
import sys
from math import copysign
from Car import Car
from CarAI import CarAI
from Map import Map

width = 1024
height = 600
pygame.display.set_caption("SuperCarRace")
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
ticks = 60

path = "assets/Map.bmp"
path2 = "assets/RewardMap.bmp"
gameMap = Map(path, path2)

car = CarAI(4.5, 9)
# car = Car(4.5, 9)
car_image = pygame.transform.scale(pygame.image.load("assets/Car.png"), (28, 16))

while True:
    dt = clock.get_time() / 300
    gameMap.refresh(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pressed = pygame.key.get_pressed()

    car.move(dt, pressed)
    car.update(dt)
    
    gameMap.refresh(screen)
    car.update_dist(screen, gameMap.map)
    rotated = pygame.transform.rotate(car_image, car.angle)
    rect = rotated.get_rect()
    car.checkCollision(rect, gameMap.map)
    screen.blit(rotated, car.position * 32 - (int(rect.width / 2), int(rect.height / 2)))
    
    #refresh window
    pygame.display.flip()
    clock.tick(ticks)
