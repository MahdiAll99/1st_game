# pygame template
import pygame
import random

WIDTH = 480
HEIGHT = 600
RED=(255,0,0)
FPS = 60

# colors
WHITE = ( 255 , 255 , 255 )
BLACK = ( 0 , 0 , 0 )
RED = ( 255 , 0 , 0 )
GREEN = ( 0 , 255 , 0 )
BLUE = ( 0 , 0 , 255)
bg=pygame.image.load('3.jpg')
bg1=pygame.image.load('2.jpg')
bg2=pygame.image.load('1.jpg')
bggo=pygame.image.load('Background3dth.png')
got_logo = pygame.image.load('egypt_png.png')
nk_pic=pygame.image.load('main_character1.png')
LeftKey=pygame.image.load('LeftKey.png')
RightKey=pygame.image.load('RightKey.png')
SpaceBar=pygame.image.load('SpaceBar.png')
dragon_pics=[pygame.image.load('Dragon4.png'),pygame.image.load('Dragon5.png'),pygame.image.load('Dragon6.png')]
# initialize pygame and create window

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("The Night King")
# music
BulletSound=pygame.mixer.Sound('bullet.wav')
HitSound=pygame.mixer.Sound('hit.wav')
music=pygame.mixer.music.load('Dark Egyptian Music - Anubis.wav')
pygame.mixer.music.play(-1) #play music all the game

clock = pygame.time.Clock()
font_name=pygame.font.match_font('arial')
def draw_text(surface,color,text,size,x,y):
    font=pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,color)
    text_rect=text_surface.get_rect()
    text_rect.midtop=(x,y)
    surface.blit(text_surface,text_rect)
    
def show_home_screen(msg1,msg2,msg3,blit):
    screen.blit(bggo,(0,0))
    screen.blit(got_logo,(110,-20))
    if blit :
        screen.blit(LeftKey,(155,HEIGHT/4+127))
        screen.blit(RightKey,(250,HEIGHT/4+127))
        screen.blit(SpaceBar,(WIDTH/2-175,HEIGHT/4+185))
    draw_text(screen,BLACK,msg1,20,WIDTH/2,HEIGHT/4+140)
    draw_text(screen,BLACK,msg2,20,WIDTH/2+30,HEIGHT/4+200)
    draw_text(screen,BLACK,msg3,22,WIDTH/2,HEIGHT/4+250)
    pygame.display.flip()
    pygame.time.wait(1000)
    waiting=True
    while waiting :
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                game_over = False
                waiting = False
    
class NightKing(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = nk_pic.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT
        self.radius=20
        #pygame.draw.circle(self.image,RED,self.rect.center,self.radius)
        self.speedx = 0
        self.lives=3
        self.visible=True

    def update(self):
        self.speedx = 0
        #pygame.draw.rect(screen,WHITE,self.rect)
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet=Bullet(self.rect.centerx,self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        
class Dragon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(dragon_pics)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.radius=int(self.rect.width/2)
        #pygame.draw.circle(self.image,RED,self.rect.center,self.radius)
        self.speedx=random.randrange(-5,5)
        self.speedy = random.randrange(1,8)
    def update(self):
        self.rect.y +=self.speedy
        self.rect.x+=self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.left<-80 or self.rect.right>WIDTH+25:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1,10)
            self.speedx=random.randrange(-5,5)
    

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('Bullet1.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.speedy=-10
        self.rect.centerx=x
        self.rect.bottom=y
    def update(self):
        self.rect.y+=self.speedy
        if self.rect.bottom<0:
            self.kill()
            
all_sprites = pygame.sprite.Group()
dragons = pygame.sprite.Group()
bullets=pygame.sprite.Group()
nk=NightKing()
all_sprites.add(nk)
for i in range(10):
   d=Dragon()
   all_sprites.add(d)
   dragons.add(d)
# Game loop
life = 0
score=0
game_over=True
running = True
msg1="PRESS              OR             TO MOVE"
msg2="SPACE BAR TO SHOOT !"
msg3="NOW PRESS ANY KEY TO START THE GAME"
while running:
         #keep loop running at right speed
    if game_over :
        show_home_screen(msg1,msg2,msg3,True)
        game_over=False
        running = True
        all_sprites = pygame.sprite.Group()
        dragons = pygame.sprite.Group()
        bullets=pygame.sprite.Group()
        nk=NightKing()
        all_sprites.add(nk)
        for i in range(10):
           d=Dragon()
           all_sprites.add(d)
           if len(dragons) < 10:
               dragons.add(d)
        # Game loop
        life = 0
        score=0
        
    clock.tick(FPS)
    #process input (events)
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                BulletSound.play()
                nk.shoot()
    # add dragons speed
    if pygame.time.get_ticks()>10000 :
        d.speedx+=1/3
        d.speedy+=1/2
    # Update
    all_sprites.update()
    # draw/ render
    if life ==0:
       screen.blit(bg,(0,0))
    elif life==-1:
        screen.blit(bg1,(0,0))
    elif life==-2:
        screen.blit(bg2,(0,0))
    else :
        game_over=True

    all_sprites.draw(screen)
    #collision
    hits=pygame.sprite.groupcollide(bullets,dragons,True,True)
    if hits:
        HitSound.play()
        score+=10
        d=Dragon()
        all_sprites.add(d)
        dragons.add(d)
    hits=pygame.sprite.spritecollide(nk,dragons,True,pygame.sprite.collide_circle)
    for hit in hits :
        #nk_pic=pygame.image.load('NightKingWasHit.png')
        life-=1
        pygame.time.wait(1000)
        d=Dragon()
        all_sprites.add(d)
        dragons.add(d)
        
    # after drawing everything
    
    draw_text(screen,BLACK,str(score),30,WIDTH/2,10)
    #score reaches its maximum : 1000
    if score==1000 :
        show_home_screen("","","YOU WON ! ",False)
    pygame.display.flip()
pygame.quit()
