import pygame
import random
import time

pygame.init()

screen_width = 900
screen_height = 700

screen = pygame.display.set_mode([screen_width, screen_height])

pygame.display.set_caption('Recycle Marathon')

def change_background():
    background=pygame.image.load("bground.png")
    bg=pygame.transform.scale(background,(screen_width, screen_height))
    screen.blit(bg,(0,0))

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('bin.png')
        self.image=pygame.transform.scale(self.image,(40,60))
        self.rect=self.image.get_rect()

class non_recyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('plastic.png')
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()
