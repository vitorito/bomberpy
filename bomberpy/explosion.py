import pygame as pg
from time import time
from .utils  import *


class Explosion(pg.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = explosion_img.subsurface([0, 0, 0, 0])
        self.rect = pg.rect.Rect([0, 0, 50, 50])
        self.start_time = time()
        self.rotate = 0
        self.subrect = [0, 0, 48, 48]
        
    def update(self):
        self.timer = time() - self.start_time
        self.animation()
            
    def animation(self):
        aux = int((self.timer - int(self.timer)) * 7 % 7)
        if aux  <= 5:
            self.subrect[0] = aux * 48
            self.image = explosion_img.subsurface(self.subrect)
            self.image = pg.transform.scale(self.image, [50, 50])
            self.image = pg.transform.rotate(self.image, self.rotate)
        else:
            self.kill()
        
    def objExplosion(self, rect):
        exp = Explosion(explosionGroup, gameObjectGroup)
        exp.rect = pg.rect.Rect(rect)
        return exp
    
    def subExplosion(self, direction, subrect, rotate, n, minus_x=0, minus_y=0):
        subrect[1] += 48 if n == self.range else 0

        x = self.rect.x - (minus_x * 50)
        y = self.rect.y - (minus_y * 50)
        exp = self.objExplosion([x, y, 50, 50])
        exp.subrect = subrect
        exp.rotate = rotate

        wall = pg.sprite.spritecollide(exp, wallGroup, False)
        block = pg.sprite.spritecollide(exp, blockGroup, False)
        bomb = pg.sprite.spritecollide(exp, bombGroup, False)

        if wall or block or bomb:
            if wall:
                wall[0].start_time = time()
                wall[0].dead = True
            if bomb:
                bomb[0].explosion()
            self.stopDirection(direction)
            exp.kill()

    def stopDirection(self, direction):
        if direction == 'top':
            self.top_collide = True
        elif direction == 'bottom':
            self.bottom_collide = True
        elif direction == 'left':
            self.left_collide = True
        elif direction == 'right':
            self.right_collide = True
            
    def generateExplosion(self):
        self.top_collide = False
        self.bottom_collide = False
        self.left_collide = False
        self.right_collide = False

        for n in range(1, self.range + 1):
            if not self.top_collide:
                self.subExplosion('top', [0, 48, 48, 48], 90, n, minus_y=n)
            if not self.bottom_collide:
                self.subExplosion('bottom', [0, 48, 48, 48], -90, n, minus_y=-n)
            if not self.left_collide:
                self.subExplosion('left', [0, 48, 48, 48], 180, n, minus_x=n)
            if not self.right_collide:
                self.subExplosion('right',[0, 48, 48, 48], 0, n, minus_x=-n)