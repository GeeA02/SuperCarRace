import pygame, math
from math import copysign
from pygame.math import Vector2
from Car import Car, Action

class CarAI (Car):
    def __init__(self,x,y,m, angle = 90, length = 0.5, max_steering = 15, max_acceleration= 2.5):
        self.startPosition = Vector2(x, y)
        self.position = Vector2(self.startPosition.x, self.startPosition.y)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = angle
        self.length = length
        self.max_acceleration = max_acceleration
        self.max_steering = max_steering
        self.max_velocity = 2.5
        self.brake_deceleration = 3
        self.free_deceleration = 2

        self.acceleration = 0.0
        self.steering = 0.0
        self.map = m
        self.distances = [] * 8
        self.dead = False

    def update_dist(self):
        a = []
        a.append(math.tan(self.angle))
        a.append(math.tan(self.angle+30))
        a.append(math.tan(self.angle+90))
        a.append(math.tan(self.angle+150))
        a.append(math.tan(self.angle+180))
        a.append(math.tan(self.angle-150))
        a.append(math.tan(self.angle-90))
        a.append(math.tan(self.angle-30))
        i=0
        
        while self.map.mapPixels[math.floor(i)][0]!=math.floor(self.position.x + i) and self.map.mapPixels[math.floor(i)][1]!=math.floor(self.position.y + math.floor(i*a[0])) :
            i+=0.1
        i=math.floor(i)
        print(math.sqrt((self.map.mapPixels[i][0]-self.position.x)**2+(self.map.mapPixels[i][1]-self.position.y)**2))

    def move(self, dt, output):
        par = 0.5
        ######### UP #############
        if output[0] > par:
            self.takeAction(Action.Accelerate, dt)
        ######### DOWN ###########
        elif output[1] > par:
            self.takeAction(Action.Reverse, dt)
        else:
            self.takeAction(Action.Decelerate, dt)

        ######## RIGHT & LEFT #########
        if output[2] > par:
            self.takeAction(Action.TurnRight, dt)
        elif output[3] > par:
            self.takeAction(Action.TurnLeft, dt)
        else:
            self.takeAction(Action.GoStraight, dt)
