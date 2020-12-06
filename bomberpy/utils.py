import pygame as pg
from os import path

CAMINHO = path.split(path.abspath(__file__))[0]
HEIGHT, WIDTH = pg.display.get_window_size()

# groups
gameObjectGroup = pg.sprite.Group()
collidingGroup = pg.sprite.Group() # grupo dos objetos colidíveis
explosionGroup = pg.sprite.Group()
bombGroup = pg.sprite.Group(gameObjectGroup) 
wallGroup = pg.sprite.Group(gameObjectGroup)

#images
player_img = pg.image.load(CAMINHO + "/images/player.png").convert_alpha()
bomb_img = pg.image.load(CAMINHO + "/images/bombsprite.png").convert_alpha()
newGame_img = pg.image.load(CAMINHO + "/images/newgame.png").convert_alpha()
wall_img = pg.image.load(CAMINHO + "/images/wall.png").convert_alpha()
explosion_img = pg.image.load(CAMINHO + "/images/explosion.png").convert_alpha()
block_img = pg.image.load(CAMINHO + "/images/block.png").convert()
mainMenu_img = pg.image.load(CAMINHO + "/images/menu.png").convert()
background_img = pg.image.load(CAMINHO + "/images/grass.png").convert()

# 0 = bloco, 1 = vazio mutável, 2 =  vazio, 3 = muro
MATRIZ = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,2,2,3,1,1,1,1,1,1,1,1,1,1,2,2,0],
    [0,2,0,3,0,1,0,1,0,1,0,1,0,1,0,2,0],
    [0,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,2,0,1,0,1,0,1,0,1,0,1,0,1,0,2,0],
    [0,2,2,1,1,1,1,1,1,1,1,1,1,1,2,2,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]