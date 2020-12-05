import pygame as pg
from .utils import newGame_img, HEIGHT, WIDTH

class NewGameBottom(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface.subsurface(newGame_img, [0, 0, 0, 0])
        self.rect = pg.rect.Rect([HEIGHT//2-100, WIDTH//1.4, 200, 50])
    
    def changeImg(self, pos):
        self.image = pg.Surface.subsurface(newGame_img, [0, pos, 60, 15])
        self.image = pg.transform.scale(self.image, [200,50])

