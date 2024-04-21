from pygame import *
from random import *


okno = display.set_mode((1200,600))
 
fps = time.Clock() #контроль fps
game = True
font.init()
wr = font.Font('shir.ttf',125)
fr = font.Font('shir.ttf',30)
class wall(sprite.Sprite):
    def __init__(self, x,y,w,h):
        self.image = Surface((w,h))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))


    
steni = [
    wall(0,0,1200,10), wall(0,590,1200,10)   
]

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
        if kn[K_s] and self.rect.y < 510:
            self.rect.y += 10
class player(gamebo):
    def move(self):
    
        self.ris()
        kn = key.get_pressed()
        if kn[K_UP] and self.rect.y > 0:
            self.rect.y -= 10
        if kn[K_DOWN] and self.rect.y < 510:
            self.rect.y += 10
farx = 5
fary = 3
ship = player('стена.png',10,200,30,120)
ship2 = player2('стена.png',1160,200,30,120)
health = 'GAME OVER'
points = 0


class player3(gamebo):
    def move(self):

        self.ris()
        
        self.rect.x += farx
        self.rect.y += fary
ball = player3('мяч.png', 600,300,30,30)
raepoints = 0
hah = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    for w in steni:
        w.ris()
    
        
        
        
    okno.fill((0,0,0)) 
    ship.ris()
    ship2.ris()
    ship.move()
    ship2.move2()
    ball.move()
    if sprite.collide_rect(ball, ship):
        farx = 5
        gag = randint(1, 2)
        #if gag == 1:
            #fary = 0
        if gag == 2:
            fary = -3
        if gag == 1:
            fary == 3
    if sprite.collide_rect(ball, ship2):
        farx = -5
        gag = randint(1, 2)
        #if gag == 1:
            #fary = 0
        if gag == 2:
            fary = -3 
        if gag == 1:
            fary == 3
    for w in steni:
            if sprite.collide_rect(ball,w):
                if ball.rect.y > 300:
                    fary = -3
                if ball.rect.y < 300:
                    fary = 3
    if ball.rect.x > 1200 or ball.rect.x <0:
       hp = wr.render(str(health), False, (139, 0, 0))
       okno.blit(hp, (225,200))
       hah = False
       
         
    raepoints += 1
    if raepoints == 50 and hah == True:
    
        points += 1
        raepoints = 0
    
    pp = fr.render(str(points),False,(255, 165, 0))
    
    okno.blit(pp, (1100,80))

               
                
    
    
    
    
    #b.fly()
    
    fps.tick(60)
    display.update()
