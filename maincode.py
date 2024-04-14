from pygame import *
from random import *

okno = display.set_mode((1200,600))
 
fps = time.Clock() #контроль fps
game = True
class gamebo(sprite.Sprite):
    def __init__(self, img, x,y,w,h):
        super().__init__()
        self.image = transform.scale(image.load(img),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lastx = self.rect.x
        self.lasty = self.rect.y
    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))
class player(gamebo):
    def move(self):
    
        self.ris()
        kn = key.get_pressed()
        if kn[K_UP] and self.rect.y > 0:
            self.rect.y -= 7
        if kn[K_DOWN] and self.rect.y < 950:
            self.rect.y += 7
ship = player('rocket.png',480,540,50,50)
