import pygame as pg
from .utils import player_img, deathPlayer_img
from .utils import wallGroup, bombGroup, blockGroup, explosionGroup, enemyGroup


class Player(pg.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = player_img.subsurface([0, 0, 16, 24])
        self.rect = pg.rect.Rect(52, 52, 40, 40)  
        self.dead = False
        self.bomb_limit = 1
        self.explosion_range = 1
        self.vel = 2.5
        self.dir = 1
        self.mov = 10
        self.UVmap = [
            [0, 34, 17], [102, 136, 119],
            [51, 85, 68], [153, 187, 170]
        ]
        self.deathUVmap = [1, 18, 35, 52, 69, 94, 119, 144, 169]

    def update(self):
        if not self.dead:
            self.animation()
            self.movement()
            self.checkDeath()
        else:
            self.deathAnimation()

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
        frame = player_img.subsurface(img_rect)
        self.image = pg.transform.scale(frame, [40, 40])

    def deathAnimation(self):
        aux = (pg.time.get_ticks() // 220) % 10
        if aux < 9:
            img_rect = [self.deathUVmap[aux], 0, 16, 25]
            if aux > 3:
                img_rect[2] = 24
            frame = deathPlayer_img.subsurface(img_rect)
            self.image = pg.transform.scale(frame, [40, 40])
        else:
            self.kill()
    
    def willCollide(self, x, y):
        temp = self.rect.center
        self.rect.x += x
        self.rect.y += y

        wall = pg.sprite.spritecollide(self, wallGroup, False)
        block = pg.sprite.spritecollide(self, blockGroup, False)
        bomb = pg.sprite.spritecollide(self, bombGroup, False)

        if bomb and self.over_last_bomb and bomb[-1] == self.last_bomb:
            bomb.pop()
        else:
            self.over_last_bomb = False

        if wall or block or bomb:
            self.rect.center = temp  

    def checkDeath(self):
        explosion = pg.sprite.spritecollide(self, explosionGroup, False)
        enemy = pg.sprite.spritecollide(self, enemyGroup, False)

        if explosion or enemy:
            self.dead = True
            self.aux = 0
