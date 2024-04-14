from pygame import *
from random import *

okno = display.set_mode((1200,600))
 
fps = time.Clock() #контроль fps
game = True
font.init()
wr = font.Font(None,30)
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
class player2(gamebo):
    def move2(self):
    
        self.ris()
        kn = key.get_pressed()
        if kn[K_w] and self.rect.y > 0:
            self.rect.y -= 7
        if kn[K_s] and self.rect.y < 950:
            self.rect.y += 7
class player(gamebo):
    def move(self):
    
        self.ris()
        kn = key.get_pressed()
        if kn[K_UP] and self.rect.y > 0:
            self.rect.y -= 7
        if kn[K_DOWN] and self.rect.y < 950:
            self.rect.y += 7
ship = player('стена.png',100,200,20,40)
ship2 = player2('стена.png',1100,200,20,40)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    okno.fill((0,0,0))
    ship.ris()
    ship2.ris()
    ship.move()
    ship2.move2()
    if sprite.collide_rect(ship,ball):
        pp += 1
    if sprite.collide_rect(ship2,ball):
        pp += 1
     
    hp = wr.render(str(health), False, (255,0,9))
    pp = wr.render(str(points),False,(200,100,44))
    okno.blit(hp, (1100,40))
    okno.blit(pp, (1100,80))
    #b.fly()
    
    fps.tick(60)
    display.update()
