import pygame as pg

from .player import Player
from .bomb import Bomb
from .block import Block
from .utils import *

pl = Player(gameObjectGroup)  

class Game(pg.sprite.Sprite):
    """ Esta classe controla somente a execução da partida, não a do programa em si"""
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = background_img
        self.image = pg.transform.scale(self.image, (HEIGHT, WIDTH)).convert()
        self.rect = self.image.get_rect()
        self.running = False
        self.generateMap()

    def update(self):
        if self.running:
            for event in pg.event.get(): 
                if event.type == pg.QUIT:
                    exit()
                if event.type == pg.KEYDOWN: 
                    if event.key == pg.K_ESCAPE:
                        self.running = False
                    if event.key == pg.K_SPACE and not pg.sprite.spritecollide(pl, bombGroup, False): 
                        if pl.bomb_limit >= len(bombGroup):  # limita as bombas
                            newBomb = Bomb(gameObjectGroup, bombGroup) 
                            newBomb.rect.center = pl.rect.center
                if event.type == pg.KEYUP:
                    if event.key in [pg.K_w, pg.K_s, pg.K_a, pg.K_d]:
                        pl.mov = 10

    def generateMap(self):
        for l in range(len(MATRIZ)):
            for c in range(len(MATRIZ[l])):
                if MATRIZ[l][c] == 'b':
                    x, y = c * 50, l * 50
                    bl = Block(blockGroup)
                    bl.rect.x, bl.rect.y = x, y
