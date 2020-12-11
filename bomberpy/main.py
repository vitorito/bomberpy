# VERSION = 0.0.2.dev1

import pygame as pg

pg.init()

display = pg.display.set_mode([850, 550]) 

from .menu import Menu
from .game import Game, gameObjectGroup, playerGroup, enemyGroup
from .utils import icon

pg.display.set_caption("Bomberpy")
pg.display.set_icon(icon)

def run():
    menuGroup = pg.sprite.Group()   
    gameGroup = pg.sprite.Group()

    mn = Menu(menuGroup)  
    gm = Game(gameGroup)

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
            for event in pg.event.get():  
                if event.type == pg.QUIT: 
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mn.click()
                        if mn.button == 'new_game':
                            gm.running = True
                            mn.button = False
                        
                menuGroup.update()
                menuGroup.draw(display)

        pg.display.update()


if __name__ == "__main__":
    run()

