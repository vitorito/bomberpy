import pygame as pg 
from random import choice as _choice
from time import time as _time
from .utils import enemy_img, MATRIZ
from .utils import wallGroup, blockGroup, bombGroup, explosionGroup

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
        self.direction = _choice(['up', 'bottom', 'left', 'right'])
        self.target = None

    def update(self):
        if not self.dead:
            self.animation()
            self.move()
            self.checkDeath()
        else:
            self.timer = _time() - self.start_time
            self.deathAnimation()
  
    def animation(self):
        aux = int(self.mov) * 16
        frame = enemy_img.subsurface([aux, 0, 16, 16])
        self.image = pg.transform.scale(frame, [45, 45])

    def deathAnimation(self):
        aux = 96 + int((self.timer - int(self.timer)) * 10 // 1.5) * 16
        if aux <= 160:
            frame = enemy_img.subsurface([aux, 0, 16, 16])
            self.image = pg.transform.scale(frame, [45, 45])
        else:
            self.kill()

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
        self.direction = _choice(list(self.directions.keys()))

    def calcTarget(self):
        x, y = self.rect.center

        if self.direction == 'up':
            self.target = x, y - 50
        if self.direction == 'bottom':
            self.target = x, y + 50
        if self.direction == 'left':
            self.target = x - 50, y    
        if self.direction == 'right':
            self.target = x + 50, y  

    def move(self):
        if self.rect.center == self.target or self.cur_dir_collide():
            self.chooseDirection()
            self.calcTarget()
            
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
    
    def checkDeath(self):
        if pg.sprite.spritecollide(self, explosionGroup, False):
            self.dead = True
            self.start_time = _time()