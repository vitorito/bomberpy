import pygame as pg 
import random
from time import time, sleep
from .utils import enemy_img, MATRIZ, wallGroup, blockGroup, bombGroup

class Enemy(pg.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = enemy_img.subsurface([0, 0, 16, 16])
        self.image = pg.transform.scale(self.image, [50, 50])
        self.rect = self.image.get_rect()
        self.dead = False
        self.vel_x = 0
        self.vel_y = 0
        self.mov = 0
        self.direction = random.choice(['up', 'bottom', 'left', 'right'])
        self.prev_pos = self.calc_pos()

    def update(self):
        if not self.dead:
            self.animation()
            self.move()
  
    def animation(self):
        aux = int(self.mov) * 16
        frame = enemy_img.subsurface([aux, 0, 16, 16])
        self.image = pg.transform.scale(frame, [50, 50])

    def collide(self, x=0, y=0, moving=False):
        temp = self.rect.center
        self.rect.x += x
        self.rect.y += y

        wall = pg.sprite.spritecollide(self, wallGroup, False)
        block = pg.sprite.spritecollide(self, blockGroup, False)
        bomb = pg.sprite.spritecollide(self, bombGroup, False)
        collide = wall or block or bomb

        if not moving or collide:
            self.rect.center = temp
        return collide != []
    
    def cur_dir_collide(self):
        self.directions = {'up':(0,-2), 'bottom':(0,2), 'left':(-2,0), 'right':(2,0)}
        x, y = self.directions[self.direction]

        return self.collide(x=x, y=y)
        

    def chooseDirection(self):
        if self.cur_dir_collide():
            self.directions.pop(self.direction)
        return random.choice(list(self.directions.keys()))

    def calc_pos(self):
        x = self.rect.x // 50
        y = self.rect.y // 50
        return x, y

    def move(self):
        cur_pos = self.calc_pos() 
        if cur_pos != self.prev_pos or self.cur_dir_collide():
            self.direction = self.chooseDirection()
            self.prev_pos = cur_pos

        if self.direction == 'up':
            self.vel_x = 0
            self.vel_y = -2
        elif self.direction == 'bottom':
            self.vel_x = 0
            self.vel_y = 2
        elif self.direction == 'left':
            self.vel_x = -2
            self.vel_y = 0
        elif self.direction == 'right':
            self.vel_x = 2
            self.vel_y = 0

        self.collide(x=self.vel_x, y=self.vel_y, moving=True)
        self.mov = (self.mov + 0.1) % 6

    def get_player(self, player):
        self.pl = player