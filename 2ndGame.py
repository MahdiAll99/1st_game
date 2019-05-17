import pygame
from random import randint 
import random 
pygame.init()
WIDTH=500
HEIGHT=480
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My 2nd Game")
Rocks=[pygame.image.load('Rock1.png'),pygame.image.load('Rock2.png'),pygame.image.load('Rock3.png'),pygame.image.load('Rock4.png')]
bg=pygame.image.load('starsbackground.png') #BackGround Biiitch
char=pygame.image.load('fighter1.png')
picture = pygame.transform.scale(bg,(500,480))
plane=pygame.transform.scale(char,(100,180))
projectile1=pygame.image.load('Bullet.png')
angle=90
rock1=pygame.image.load('Rock1.png').convert()
rock2=pygame.image.load('Rock2.png')
rock3=pygame.image.load('Rock3.png')
rock4=pygame.image.load('Rock4.png')
#rocks=[pygame.image.load('Rock1.png'),pygame.image.load('Rock2.png'),pygame.image.load('Rock3.png'),pygame.image.load('Rock4.png')]
rocksrotation=[pygame.transform.rotate(pygame.image.load('Rock1.png'),angle),pygame.transform.rotate(pygame.image.load('Rock2.png'),angle),pygame.transform.rotate(pygame.image.load('Rock3.png'),angle),pygame.transform.rotate(pygame.image.load('Rock4.png'),angle)]

clock=pygame.time.Clock()
a=randint(0,3)
b=randint(0,200)
keys=pygame.key.get_pressed()
class fighter(pygame.sprite.Sprite):
    def __init__(self):
        self.image=plane
        self.rect=self.image.get_rect()
        self.rect.centerx=WIDTH/2
        self.rect.bottom=HEIGHT=-10
        self.vel=0
        

    def draw(self):
        self.vel=0
        if keys[pygame.K_RIGHT]:        
           self.vel=5
        if keys[pygame.K_LEFT]:
            self.vel=-5

        win.rect.x+=self.vel
        


class projectile(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=15
        self.hitbox=(self.x,self.y,50,50)
    def drawbullet(self,win):
         win.blit(projectile1,(self.x,self.y))
         #pygame.draw.rect(win,(255,0,0),(self.hitbox[0]+50,self.hitbox[1]-30,20,60))
         self.hitbox=(self.x-30,self.y+30,0,0)
class fighter(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=15
        self.hitbox=(self.x,self.y,50,50)
    def draw(self,win):
         win.blit(projectile1,(self.x,self.y))
         #pygame.draw.rect(win,(255,0,0),(self.hitbox[0]+50,self.hitbox[1]-30,20,60))
         self.hitbox=(self.x-30,self.y+30,0,0)
        



        
class rock(object):
    def __init__(self,x,y,width,height,a):
        self.a=a
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=8
        self.visible=True
        self.hitbox=(self.x,self.y,50)
    def drawrock(self,win):
        if (self.visible):
            win.blit(rocksrotation[a],(self.x,self.y))         
            #pygame.draw.rect(win,(255,0,0),(self.hitbox[0]+60,self.hitbox[1],60,60))
            self.hitbox=(self.x-30,self.y+30,0,0)
  


    
def drawGame():
    win.blit(picture,(0,0))
    ship.draw(win)
    rockstab[0].drawrock(win)
    #test.drawbullet(win)===> works!
    for bullet in bullets:
        bullet.drawbullet(win)
    pygame.display.update()

    
bullets=[]
myrock=rock(0,b,50,50,a)
rockstab=[myrock]
#test=projectile(200,310,150,150)
#=projectile(200,310,150,150)

ship=fighter(100,100,100,50)

run = True
while run:
    w=100
    h=100
    #myrock=rock(0,b,50,50,a)
    rocksrotation=[pygame.transform.scale(pygame.transform.rotate(pygame.image.load('Rock1.png'),angle),(w,h)),pygame.transform.scale(pygame.transform.rotate(pygame.image.load('Rock2.png'),angle),(w,h)),pygame.transform.scale(pygame.transform.rotate(pygame.image.load('Rock3.png'),angle),(w,h)),pygame.transform.scale(pygame.transform.rotate(pygame.image.load('Rock4.png'),angle),(w,h))]
    angle+=20
    b=randint(0,200)
    clock.tick(60)

    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    for bullet in bullets:
        for rock in rockstab:
            if rock.y-100<bullet.hitbox[1]-60 and rock.y+50>bullet.hitbox[1]-30:
                  if rock.x-20<rock.hitbox[1]+60 and rock.x+20>rock.hitbox[1]:
                      rock.visible=False
                      bullets.pop(bullets.index(bullet))
                      
        if bullet.y<0:
           bullets.pop(bullets.index(bullet))
        else:
            bullet.y-=bullet.vel
    for myrocks in rockstab:
        myrocks.x+=myrocks.vel
        if myrocks.x>450:
            a=randint(0,3)            
            rockstab.pop(rockstab.index(myrocks))
            rockstab.append(myrock)
            rock.visible=True
            myrocks.x=0
           
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        #print('left')
        ship.x-=ship.vel
    if keys[pygame.K_RIGHT]:
        #print('right')
        ship.x+=ship.vel
    if keys[pygame.K_SPACE]:
            i=0
            if len(bullets)<3:
                bullets.append(projectile(ship.x+20,ship.y-70,150,150)) 
                while i<10:
                    pygame.time.delay(10)
                    i+=1        
    drawGame()
    
pygame.quit()
