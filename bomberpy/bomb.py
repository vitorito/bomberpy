import pygame as pg
from time import time
from .explosion import Explosion
from .utils import bomb_img, explosionGroup, gameObjectGroup


class Bomb(pg.sprite.Sprite):
    """ Cria os objetos de bomba, controla a sua explosão e animação"""
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = bomb_img.subsurface([0, 0, 0, 0])
        self.rect = pg.rect.Rect([0, 0, 40, 50])
        self.start_time = pg.time.get_ticks()
        self.range = 1

    def update(self):
        self.timer = pg.time.get_ticks() - self.start_time
        if self.timer >= 3500:
            self.explosion()
        else:
            self.animation()
            
    def animation(self):
        aux = (self.timer // 160) % 4
        self.image = pg.Surface.subsurface(bomb_img, [aux * 80, 0 , 80, 120])
        self.image = pg.transform.scale(self.image, [40, 50])
        
    def explosion(self):
        exp = Explosion(explosionGroup, gameObjectGroup)
        exp.rect.center = self.rect.center
        exp.range = self.range
        self.kill()
        exp.generateExplosion()
        
        
    def calcPos(self, pos):
        x = (pos[0] // 50) * 50 + 25
        y = (pos[1] // 50) * 50 + 25
        self.rect.center = x, y

