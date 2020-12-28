# VERSION = 0.0.4.dev1

import pygame as pg

pg.init()

display = pg.display.set_mode([850, 550]) 

from .menu import Menu
from .game import Game
from .utils import icon, menuGroup
from .utils import gameObjectGroup, playerGroup, enemyGroup

pg.display.set_caption("Bomberpy")
pg.display.set_icon(icon)
 
def run():
    mn = Menu(menuGroup)
    gm = Game()
    mn.get_game(gm)

    clock = pg.time.Clock()
    while True:
        clock.tick(30) 
        if gm.dead:
            gm.reset()
            gm = Game()
            mn.get_game(gm)
            mn.playMusic()
        elif gm.running: 
            gm.update()
            gm.draw(display)
        else:
            menuGroup.update()
            menuGroup.draw(display)

        pg.display.flip()


if __name__ == "__main__":
    run()
