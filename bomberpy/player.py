import pygame as pg
from .utils import player_img, collidingGroup


class Player(pg.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pg.Surface([40, 40])
        self.rect = pg.rect.Rect(52, 52, 40, 40)  
        self.bomb_limit = 50 
        self.vel = 4
        self.dir, self.mov = 1, 10
        self.UVmap = [[0, 34, 17], [102, 136, 119],
                     [51, 85, 68], [153, 187, 170]]

    def update(self):
        self.animation()
        self.movement()

    def movement(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            self.willCollide(0, -self.vel)
            if not (keys[pg.K_a] or keys[pg.K_d]):
                self.dir = 0
                self.mov += 3
        if keys[pg.K_s]:
            self.willCollide(0, self.vel)
            if not (keys[pg.K_a] or keys[pg.K_d]):
                self.dir = 1
                self.mov -= 3
        if  keys[pg.K_a]:
            self.willCollide(-self.vel, 0)
            self.dir = 2
            self.mov -= 3
        if keys[pg.K_d]:
            self.willCollide(self.vel, 0)
            self.dir = 3
            self.mov += 3
        self.mov %= 30 

    def animation(self):
        img_rect = [self.UVmap[self.dir][self.mov//10], 0 , 16, 24]
        self.image = pg.Surface.subsurface(player_img, img_rect)
        self.image = pg.transform.scale(self.image, [40, 40])
    
    def willCollide(self, x, y):
        temp = self.rect.center
        self.rect.x += x
        self.rect.y += y

        if pg.sprite.spritecollide(self, collidingGroup, False):
            self.rect.center = temp  

    