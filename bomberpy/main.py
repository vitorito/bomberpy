# VERSION = 0.0.3.dev1

import pygame as pg

pg.init()

display = pg.display.set_mode([850, 550]) 

from .menu import Menu
from .game import Game
from .utils import icon, menuGroup, gameGroup
from .utils import gameObjectGroup, playerGroup, enemyGroup

pg.display.set_caption("Bomberpy")
pg.display.set_icon(icon)

def run():
    gm = Game(gameGroup)
    mn = Menu(menuGroup)
    mn.getGame(gm)  

    clock = pg.time.Clock()
    while True:
        clock.tick(30) 
        if gm.running: 
            gameObjectGroup.update()
            gameGroup.update()
            enemyGroup.update()
            playerGroup.update()
            gameGroup.draw(display)
            gameObjectGroup.draw(display)
            enemyGroup.draw(display)
            playerGroup.draw(display)
        else:
            menuGroup.update()
            menuGroup.draw(display)

        pg.display.flip()


if __name__ == "__main__":
    run()
