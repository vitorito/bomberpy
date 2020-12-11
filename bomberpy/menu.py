import pygame as pg

from .bottons import *
from .utils import mainMenu_img, HEIGHT, WIDTH


ng_bottom = NewGameBottom()

class Menu(pg.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pg.transform.scale(mainMenu_img, (HEIGHT, WIDTH))
        self.rect = self.image.get_rect()
        self.button = None
    

    def update(self):
        self.m_pos = pg.mouse.get_pos()
        if ng_bottom.rect.collidepoint(self.m_pos):
            ng_bottom.changeImg(14)
        else:
            ng_bottom.changeImg(0)
        self.image.blit(ng_bottom.image, (HEIGHT//2-100, WIDTH//1.4))

    def click(self):
        if ng_bottom.rect.collidepoint(self.m_pos):
            self.button = "new_game"
        

class SecondaryMenu(pg.sprite.Sprite):
    """ menu de pausa de quando o jogo tá em execussão """
    def __init__(self, *groups):
        super().__init__(groups)
        self.image = pg.image.load(CAMINHO + "images/secondaryMenu.png")
        self.image = pg.transform.scale(self.image, (HEIGHT, WIDTH))
        self.rect = self.image.get_rect()
