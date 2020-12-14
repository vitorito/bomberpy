import pygame as pg
from time import time as _time
from random import randint as _randint, choice as _choice
from .boosters import *
from .utils import wall_img, explosionGroup, gameObjectGroup


class Wall(pg.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = wall_img.subsurface([0, 1, 16, 15])
        self.image = pg.transform.scale(self.image, [50, 50])
        self.rect = self.image.get_rect()
        self.dead = False
        
    def update(self):
        if self.dead:
            self.timer = _time() - self.start_time
            self.deathAnimation()

    def deathAnimation(self):
        aux = 1 + int((self.timer - int(self.timer)) * 10 % 7)
        frame = wall_img.subsurface([aux * 16, 1, 16, 15])
        self.image = pg.transform.scale(frame, [50, 50])
        if aux >= 6:
            self.chooseBooster()
            self.kill()
    
    def start(self):
        self.dead = True
        self.start_time = _time()
    
    def chooseBooster(self):
        probs = _randint(0, 4)
        if probs != 0:
            return
        bst = _choice(['add_bomb', 'add_explosion_range', 'add_speed'])
        booster = Booster(bst, gameObjectGroup)
        booster.rect.center = self.rect.center
        