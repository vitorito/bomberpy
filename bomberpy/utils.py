import pygame as pg
from os import path

CAMINHO = path.split(path.abspath(__file__))[0]
HEIGHT, WIDTH = pg.display.get_window_size()

# groups
gameObjectGroup = pg.sprite.Group() 
bombGroup = pg.sprite.Group(gameObjectGroup) 
blockGroup = pg.sprite.Group(gameObjectGroup)

#images
player_img = pg.image.load(CAMINHO + "/images/player.png")
bomb_img = pg.image.load(CAMINHO + "/images/bombsprite.png")
newGame_img = pg.image.load(CAMINHO + "/images/newgame.png")
block_img = pg.image.load(CAMINHO + "/images/block.png").convert()
mainMenu_img = pg.image.load(CAMINHO + "/images/menu.png").convert()
background_img = pg.image.load(CAMINHO + "/images/grass.png").convert()


MATRIZ = [
    "bbbbbbbbbbbbbbbbb",
    "b...............b",
    "b.b.b.b.b.b.b.b.b",
    "b...............b",
    "b.b.b.b.b.b.b.b.b",
    "b...............b",
    "b.b.b.b.b.b.b.b.b",
    "b...............b",
    "b.b.b.b.b.b.b.b.b",
    "b...............b",
    "bbbbbbbbbbbbbbbbb",
]
