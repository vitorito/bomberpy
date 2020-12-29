import pygame as pg
from os import path as _path

PATH = _path.split(_path.abspath(__file__))[0]
HEIGHT, WIDTH = pg.display.get_window_size()

# groups
menuGroup = pg.sprite.Group()
gameObjectGroup = pg.sprite.Group()
explosionGroup = pg.sprite.Group()
blockGroup = pg.sprite.Group()
bombGroup = pg.sprite.Group() 
wallGroup = pg.sprite.Group()
enemyGroup = pg.sprite.Group()
playerGroup = pg.sprite.Group()

#images
icon = pg.image.load(PATH + "/images/icon.png").convert_alpha()
player_img = pg.image.load(PATH + "/images/player.png").convert_alpha()
deathPlayer_img = pg.image.load(PATH + "/images/deathplayer.png").convert_alpha()
enemy_img = pg.image.load(PATH + "/images/enemy.png").convert_alpha()
bomb_img = pg.image.load(PATH + "/images/bomb.png").convert_alpha()
white_bomb_img = pg.image.load(PATH + "/images/white_bomb.png").convert_alpha()
wall_img = pg.image.load(PATH + "/images/wall.png").convert_alpha()
explosion_img = pg.image.load(PATH + "/images/explosion.png").convert_alpha()
bomberman_img = pg.image.load(PATH + "/images/bomberman.png").convert_alpha()
pause_buttons = pg.image.load(PATH + "/images/pause_buttons.png").convert_alpha()
gameOver_img = pg.image.load(PATH + "/images/game_over.png").convert_alpha()
boosters_img = pg.image.load(PATH + "/images/boosters.png").convert()
block_img = pg.image.load(PATH + "/images/block.png").convert()
mainMenu_img = pg.image.load(PATH + "/images/mainmenu.png").convert()
background_img = pg.image.load(PATH + "/images/grass.png").convert()

#sounds
explosion_sound = pg.mixer.Sound(PATH + "/sounds/explosion_sound.wav")

# 0 = bloco, 1 = vazio mutável, 2 =  vazio, 3 = muro, 4 = inimigo
MATRIZ = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,2,2,3,1,1,1,1,1,1,1,1,1,1,2,4,0],
    [0,2,0,3,0,1,0,1,0,1,0,1,0,1,0,2,0],
    [0,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,0,1,0,2,0,1,0,1,0,2,0,1,0,1,0],
    [0,1,1,1,2,4,2,1,1,1,2,4,2,1,1,1,0],
    [0,1,0,1,0,2,0,1,0,1,0,2,0,1,0,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,2,0,1,0,1,0,1,0,1,0,1,0,1,0,2,0],
    [0,4,2,1,1,1,1,1,1,1,1,1,1,1,2,4,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
