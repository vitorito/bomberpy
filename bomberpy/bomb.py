import pygame as pg
from time import time
from .explosion import Explosion
from .utils import bomb_img, explosionGroup, gameObjectGroup


class Bomb(pg.sprite.Sprite):
    """ Cria os objetos de bomba, controla a sua explosão e animação"""
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pg.Surface.subsurface(bomb_img, [0, 0, 0, 0])
        self.rect = pg.rect.Rect([0, 0, 40, 40]) 
        self.start_time = time()  # pega o momento em que a bomba foi colocada
        self.range = 1
        self.UVmap = [0, 16, 32, 16]

    def update(self):
        self.timer = time() - self.start_time
        if self.timer >= 3:
            self.explosion()
        else:
            self.animation()
            
    def animation(self):
        aux = int((self.timer - int(self.timer)) * 10 // 2 % 4)
        img_rect = [self.UVmap[aux], 0 , 16, 16]
        self.image = pg.Surface.subsurface(bomb_img, img_rect)
        self.image = pg.transform.scale(self.image, [40, 40])
        
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




    


        


    

        
        

