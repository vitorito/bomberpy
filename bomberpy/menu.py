import pygame as pg
from time import time as _time
from .utils import menuGroup, mainMenu_img, bomberman_img, bomb_img
from .utils import HEIGHT, WIDTH, PATH, click, choose


class Menu(pg.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pg.transform.scale(mainMenu_img, (HEIGHT, WIDTH))
        self.rect = self.image.get_rect()
        self.button = None
        self.volume = 0.8

        self.bomber = Bomberman(menuGroup)
        self.bomb = Bomb(menuGroup)

        self.playMusic()

    def update(self):
        self.events()

    def events(self):
        for event in pg.event.get():  
            if event.type == pg.QUIT: 
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == 13:
                    choose.play()
                    if self.bomb.UVpos == 0:
                        self.gm.playMusic()
                        self.gm.running = True
                    elif self.bomb.UVpos == 1:
                        pass
                    elif self.bomb.UVpos == 2:
                        pass
                elif event.key == pg.K_UP:
                    self.bomb.UVpos = (self.bomb.UVpos - 1) % 3
                    click.play()
                elif event.key == pg.K_DOWN:
                    self.bomb.UVpos = (self.bomb.UVpos + 1) % 3
                    click.play()

    def playMusic(self):
        pg.mixer.music.load(PATH + "/sounds/samba_de_janeiro.wav")
        pg.mixer.music.set_volume(self.volume)
        pg.mixer.music.play(-1)

    def getGame(self, game):
        self.gm = game


class Bomberman(pg.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = bomberman_img.subsurface([0, 0, 300, 300])
        self.image = pg.transform.scale(self.image, [225, 225])
        self.rect = pg.rect.Rect([320, 200, 225, 225])

    def update(self):
        aux = (pg.time.get_ticks() // 160) % 4
        frame = bomberman_img.subsurface([aux * 300, 0, 300, 300])
        self.image = pg.transform.scale(frame, [225, 225])


class Bomb(pg.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = bomb_img.subsurface([0, 0, 80, 120])
        self.image = pg.transform.scale(self.image, [40, 60])
        self.rect = pg.rect.Rect([234, 325, 100, 100])
        self.UVmap = [(345, 272), (310, 325), (300, 376)]
        self.UVpos = 0

    def update(self):
        self.animation()
        self.rect.center = self.UVmap[self.UVpos]

    def animation(self):
        aux = (pg.time.get_ticks() // 150) % 4
        frame = bomb_img.subsurface([aux * 80, 0, 80, 120])
        self.image = pg.transform.scale(frame, [45, 60])
        