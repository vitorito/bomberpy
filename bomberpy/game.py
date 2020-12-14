import pygame as pg
from time import time
from random import random

from .player import Player
from .bomb import Bomb
from .block import Block
from .wall import Wall
from .enemy import Enemy
from .utils import *
 

class Game(pg.sprite.Sprite):
    """ Esta classe controla somente a execução da partida, não a do programa em si"""
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pg.transform.scale(background_img, (HEIGHT, WIDTH)).convert()
        self.rect = self.image.get_rect()
        self.running = False
        self.generateMap()
        self.pl = Player(playerGroup)

    def update(self):
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN: 
                if event.key == pg.K_ESCAPE:
                    self.running = False
                if event.key == pg.K_SPACE and not pg.sprite.spritecollide(self.pl, bombGroup, False): 
                    if self.pl.bomb_limit > len(bombGroup):  # limita as bombas
                        newBomb = Bomb(gameObjectGroup, bombGroup) 
                        newBomb.calcPos(self.pl.rect.center)
                        newBomb.range = self.pl.bomb_limit
                        self.pl.last_bomb = newBomb
                        self.pl.over_last_bomb = True
                    
            if event.type == pg.KEYUP:
                if event.key in [pg.K_w, pg.K_s, pg.K_a, pg.K_d]:
                    self.pl.mov = 10
    
    def generateMap(self):
        for l, line in enumerate(MATRIZ):
            for c, char in enumerate(line):
                x, y = (c * 50) + 25, (l * 50) + 25
                if char == 0:
                    bl = Block(blockGroup, gameObjectGroup)
                    bl.rect.center = x, y
                elif char == 3 or (char == 1 and random() <= 0.6):
                    wl = Wall(wallGroup, gameObjectGroup)
                    wl.rect.center = x, y
                    MATRIZ[l][c] = 3
                elif char == 4:
                    en = Enemy(enemyGroup)
                    en.rect.center = x, y
