import pygame as pg
from os import path

CAMINHO = path.split(path.abspath(__file__))[0]
HEIGHT, WIDTH = pg.display.get_window_size()

# groups
menuGroup = pg.sprite.Group()   
gameGroup = pg.sprite.Group()
gameObjectGroup = pg.sprite.Group()
explosionGroup = pg.sprite.Group()
blockGroup = pg.sprite.Group()
bombGroup = pg.sprite.Group() 
wallGroup = pg.sprite.Group()
enemyGroup = pg.sprite.Group()
playerGroup = pg.sprite.Group()

#images
icon = pg.image.load(CAMINHO + "/images/icon.png").convert_alpha()
player_img = pg.image.load(CAMINHO + "/images/player.png").convert_alpha()
deathPlayer_img = pg.image.load(CAMINHO + "/images/deathplayer.png").convert_alpha()
enemy_img = pg.image.load(CAMINHO + "/images/enemy.png").convert_alpha()
bomb_img = pg.image.load(CAMINHO + "/images/bomb.png").convert_alpha()
wall_img = pg.image.load(CAMINHO + "/images/wall.png").convert_alpha()
explosion_img = pg.image.load(CAMINHO + "/images/explosion.png").convert_alpha()
bomberman_img = pg.image.load(CAMINHO + "/images/bomberman.png").convert_alpha()
boosters_img = pg.image.load(CAMINHO + "/images/boosters.png").convert()
block_img = pg.image.load(CAMINHO + "/images/block.png").convert()
mainMenu_img = pg.image.load(CAMINHO + "/images/mainmenu.png").convert()
background_img = pg.image.load(CAMINHO + "/images/grass.png").convert()

# 0 = bloco, 1 = vazio mutável, 2 =  vazio, 3 = muro
MATRIZ = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,2,2,3,1,1,1,1,1,1,1,1,1,1,2,4,0],
    [0,2,0,3,0,1,0,1,0,1,0,1,0,1,0,2,0],
    [0,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,2,0,1,0,1,0,1,0,1,0,1,0,1,0,2,0],
    [0,4,2,1,1,1,1,1,1,1,1,1,1,1,2,4,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
