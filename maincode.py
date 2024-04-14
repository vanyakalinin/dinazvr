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
            self.rect.y -= 10
        if kn[K_s] and self.rect.y < 600:
            self.rect.y += 10
class player(gamebo):
    def move(self):
    
        self.ris()
        kn = key.get_pressed()
        if kn[K_UP] and self.rect.y > 0:
            self.rect.y -= 10
        if kn[K_DOWN] and self.rect.y < 600:
            self.rect.y += 10
farx = 20
fary = 5
ship = player('стена.png',0,200,50,90)
ship2 = player2('стена.png',1150,200,50,90)
ball = player3('мяч.png', 600,300,30,30)

class player3(gamebo):
    def move(self):

        self.ris()
        
        self.rect.x += farx
        self.rect.y += fary

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
        
        health -= 10 
        
    okno.fill((0,0,0)) 
    ship.ris()
    ship2.ris()
    ship.move()
    ship2.move2()
    ball.move()
    if sprite.collide_rect(ball, ship):
        farx = farx + 2*farx
        gag = random(1, 3)
        if gag == 1:
            fary = fary + 2*fary
        if gag == 2:
            fary = fary + 2 
        if gag == 3:
            fary == fary - 2
        if sprite.collide_rect(ball, ship2):
            farx = farx + 2*farx
        gag = random(1, 3)
        if gag == 1:
            fary = fary + 2*fary
        if gag == 2:
            fary = fary + 2 
        if gag == 3:
            fary == fary - 2
    
    pp = wr.render(str(points),False,(200,100,44))
    
    okno.blit(pp, (1100,80))
    #b.fly()
    
    fps.tick(60)
    display.update()
