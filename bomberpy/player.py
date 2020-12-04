import pygame as pg
from .utils import player_img, blockGroup


class Player(pg.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pg.Surface([40, 40])
        self.rect = pg.rect.Rect(52, 52, 40, 40)  
        self.bomb_limit = 50 
        self.dir, self.mov = 1, 10
        self.pos = [[0, 34, 17], [102, 136, 119],
                    [51, 85, 68], [153, 187, 170]]


    def update(self):
        self.animation()
        self.movement()

    def movement(self):
        keys = pg.key.get_pressed()
        w = keys[pg.K_w]
        s = keys[pg.K_s]
        a = keys[pg.K_a]
        d = keys[pg.K_d]

        if w and self.willCollide(0, -5):
            self.dir = 0
            if not (a or d):
                self.mov += 3
        if s and self.willCollide(0, 5):
            self.dir = 1
            if not (a or d):
                self.mov -= 3
        if  a and self.willCollide(-5, 0):
            self.dir = 2
            self.mov -= 3
        if d and self.willCollide(5, 0):
            self.dir = 3
            self.mov += 3
        self.mov %= 30 


    def animation(self):
        img_rect = [self.pos[self.dir][self.mov//10], 0 , 16, 24]
        self.image = pg.Surface.subsurface(player_img, img_rect)
        self.image = pg.transform.scale(self.image, [40, 40])
    

    def willCollide(self, x, y):
        temp = self.rect.center
        self.rect.x += x
        self.rect.y += y

        if pg.sprite.spritecollide(self, blockGroup, False):
            self.rect.center = temp
        return True

    