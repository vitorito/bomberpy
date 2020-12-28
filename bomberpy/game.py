import pygame as pg
from time import time
from random import random

from .player import Player
from .menu import MenuBomb
from .bomb import Bomb
from .block import Block
from .wall import Wall
from .enemy import Enemy
from .utils import *
 

class Game(object):
    """ Esta classe controla somente a execução da partida, não a do programa em si"""
    def __init__(self):
        self.image = pg.transform.scale(background_img, (HEIGHT, WIDTH)).convert()
        self.running = False
        self.dead = False

        self.restart()

    def update(self):
        if self.pm.paused:
            self.pm.update()
        else:
            self.events()
            gameObjectGroup.update()
            enemyGroup.update()
            playerGroup.update()
    
    def draw(self, display):
        display.blit(self.image, [0, 0])
        gameObjectGroup.draw(display)
        enemyGroup.draw(display)
        playerGroup.draw(display)
        if self.pm.paused:
            self.pm.draw(display)

    def events(self):
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN: 
                if event.key == pg.K_ESCAPE:
                    self.pm.paused = True
                    pg.mixer.music.pause()
                if event.key == pg.K_SPACE and not pg.sprite.spritecollide(self.pl, bombGroup, False): 
                    if self.pl.bomb_limit > len(bombGroup):  # limita as bombas
                        newBomb = Bomb(gameObjectGroup, bombGroup) 
                        newBomb.calcPos(self.pl.rect.center)
                        newBomb.range = self.pl.explosion_range
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
                elif char == 3 or (char == 1 and random() <= 0.7):
                    wl = Wall(wallGroup, gameObjectGroup)
                    wl.rect.center = x, y
                elif char == 4:
                    en = Enemy(enemyGroup)
                    en.rect.center = x, y
    
    def playMusic(self):
        pg.mixer.music.load(PATH + "/sounds/ievan_polka.wav")
        pg.mixer.music.play(-1)

    def reset(self):
        del self.pl
        del self.pm
        playerGroup.empty()
        gameObjectGroup.empty()
        enemyGroup.empty()
        wallGroup.empty()
        blockGroup.empty()

    def restart(self):
        self.pl = Player(playerGroup)
        self.pm = PauseMenu(self)
        self.generateMap()

    def __del__(self):
        print("jogo morreu")


class PauseMenu(object):
    def __init__(self, game, *groups):
        super().__init__(*groups)
        self.image = pg.surface.Surface([HEIGHT, WIDTH])
        self.image.set_alpha(240)
        self.rect = self.image.get_rect()
        self.gm = game
        self.paused = False

        self.bomb = MenuBomb()
        self.bomb.original_img = white_bomb_img
        self.bomb.UVmap = [(230, 92), (232, 147), (300, 206), (141, 263)]

    def update(self):
        self.events()
        self.bomb.update()

    def draw(self, display):
        display.blit(self.image, [0, 0])
        display.blit(pause_buttons, [40, 25])
        display.blit(self.bomb.image, self.bomb.UVmap[self.bomb.UVpos])

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.bomb.UVpos = 0
                    self.resume()
                elif event.key == pg.K_RETURN:
                    if self.bomb.UVpos == 0:
                        self.resume()
                    elif self.bomb.UVpos == 1:
                        self.restarter()
                    elif self.bomb.UVpos == 2:
                        self.back_to_menu()
                    elif self.bomb.UVpos == 3:
                        exit()
                elif event.key == pg.K_UP:
                    self.bomb.UVpos = (self.bomb.UVpos - 1) % 4
                elif event.key == pg.K_DOWN:
                    self.bomb.UVpos = (self.bomb.UVpos + 1) % 4

    def resume(self):
        self.paused = False
        self.bomb.UVpos = 0
        pg.time.wait(100)
        pg.mixer.music.unpause()

    def restarter(self):
        self.gm.reset()
        self.gm.restart()
        pg.mixer.music.play(-1)
        pg.time.wait(100)
    
    def back_to_menu(self):
        self.gm.running = False
        self.gm.dead  = True
        