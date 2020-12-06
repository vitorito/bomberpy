import pygame as pg
from time import time
from .utils import wall_img


class Wall(pg.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pg.Surface.subsurface(wall_img, [0, 1, 16, 15])
        self.image = pg.transform.scale(self.image, [50, 50])
        self.rect = self.image.get_rect()
        self.dead = False
        self.start_time = None
        
    def update(self):
        if self.dead:
            self.timer = time() - self.start_time
            self.deathAnimation()

    def deathAnimation(self):
        aux = 1 + int((self.timer - int(self.timer)) * 10 % 7)
        frame = pg.Surface.subsurface(wall_img, [aux*16, 1, 16, 15])
        self.image = pg.transform.scale(frame , [50, 50])
        if aux >= 6:
            self.kill()
        
        