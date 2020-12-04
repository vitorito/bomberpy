import pygame as pg
from time import time
from .utils import bomb_img

class Bomb(pg.sprite.Sprite):
    """ Cria os objetos de bomba, controla a sua explosão e animação"""
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pg.Surface([40, 40])
        self.rect = self.image.get_rect()
        self.explosion_range = 1 
        self.start_time = time()  # pega o momento em que a bomba foi colocada
        self.pos = [0, 16, 32, 16]

    def update(self):
        self.timer = time() - self.start_time
        if self.timer >= 5:
            self.explosion()
        else:
            self.animation()
            
    def animation(self):
        aux = int((self.timer - int(self.timer)) * 10 // 2 % 4)
        img_rect = [self.pos[aux], 0 , 16, 16]
        self.image = pg.Surface.subsurface(bomb_img, img_rect)
        self.image = pg.transform.scale(self.image, [40, 40])
        
       
    def explosion(self):
        self.kill()
        

        
        
        

