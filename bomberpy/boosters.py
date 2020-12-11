import pygame as pg
from time import time as _time
from .utils import boosters_img, playerGroup, explosionGroup

class Booster(pg.sprite.Sprite):
    def __init__(self, booster_type, *groups):
        super().__init__(*groups)
        self.booster_type = booster_type
        self.start_time = _time()
        self.changeCharacteristics()
        

    def update(self):
        self.timer = _time() - self.start_time

        player_collide = pg.sprite.spritecollide(self, playerGroup, False)
        explosion_collide = pg.sprite.spritecollide(self, explosionGroup, False)

        if player_collide:
            if self.booster_type == 'add_bomb':
                player_collide[0].bomb_limit += 1
            elif self.booster_type == 'add_explosion_range':
                player_collide[0].explosion_range += 1
            elif self.booster_type == 'add_speed':
                player_collide[0].vel += 1
            self.kill()
        elif explosion_collide or self.timer >= 5:
            self.kill()

    def changeCharacteristics(self):
        if self.booster_type == 'add_bomb':
            frame = boosters_img.subsurface([0, 0, 16, 16])
        elif self.booster_type == 'add_explosion_range':
            frame = boosters_img.subsurface([16, 0, 16, 16])
        elif self.booster_type == 'add_speed':
            frame = boosters_img.subsurface([32, 0, 16, 16])

        self.image = pg.transform.scale(frame, [40, 40])
        self.rect = self.image.get_rect()