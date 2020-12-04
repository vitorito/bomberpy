# VERSION = 0.0.1 

import pygame as pg

pg.init()

display = pg.display.set_mode([850, 550]) 
pg.display.set_caption("Bomberpy") 

from .menu import Menu
from .game import Game, gameObjectGroup, blockGroup

menuGroup = pg.sprite.Group()  
gameGroup = pg.sprite.Group()  

mn = Menu(menuGroup)  
gm = Game(gameGroup)

clock = pg.time.Clock()

def run():
    while True:
        clock.tick(30) 
        if gm.running: 
            gameGroup.update()
            gameObjectGroup.update()
            gameGroup.draw(display)
            gameObjectGroup.draw(display)
            blockGroup.draw(display)
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

