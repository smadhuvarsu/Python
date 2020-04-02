import pygame
import random
import os

WIDTH = 1000
HEIGHT = 500
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
CYAN = (0,255,255)
GOOD_GREEN=(0, 255, 34)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge Game Instuctions:Use the arrow keys to dodge the red enemies.Get your cyan Player to the green Safe Zone!")
clock = pygame.time.Clock()

pygame.mixer.music.load('bensound-happyrock.mp3')
pygame.mixer.music.play(-1)



# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((10,20))
        #self.image=pygame.image.load("Boochi_Straight.png").convert()
        self.image.fill(CYAN)
        self.rect=self.image.get_rect()
        self.rect.centerx=WIDTH/2
        self.rect.top=HEIGHT-25
        self.speedx=0

    def update(self):
        self.speedx=0
        self.speedy=0
        keys=pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left>0+5:
            self.speedx=-5
 
        if keys[pygame.K_RIGHT] and self.rect.right<WIDTH-5:
            self.speedx=5

        if keys[pygame.K_UP] and self.rect.top>0+5:
            self.speedy=-5

        if keys[pygame.K_DOWN] and self.rect.bottom<HEIGHT-5:
            self.speedy=5


        self.rect.x +=self.speedx
        self.rect.y += self.speedy

#Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((5,20))
        self.image.fill(RED)
        #self.image=pygame.image.load("apple1.png").convert()
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(0,WIDTH-self.rect.width)
        self.rect.y=random.randrange(10,50)
        self.speedy=random.randrange(2,10) 

    def update(self):
        self.rect.y+=self.speedy
        if self.rect.top > HEIGHT-10:
            self.rect.x=random.randint(0,WIDTH-self.rect.width)
            self.rect.y=random.randrange(10,50)
            self.speedy=random.randrange(1,8)

#Home_Bar class
class Home_Bar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((1000,20))
        self.image.fill(GOOD_GREEN)
        self.rect=self.image.get_rect()
        self.rect.top=0  
            
all_sprites = pygame.sprite.Group()
player=Player()
all_sprites.add(player)
enemies = pygame.sprite.Group()
hb=Home_Bar()
hbb=pygame.sprite.Group()
hbb.add(hb)
all_sprites.add(hb)

pygame.time.delay(1080)

for i in range(110):
    e=Enemy()
    all_sprites.add(e)
    enemies.add(e)
    
# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    #Check if Player and Enemy are colliding
    collisions=pygame.sprite.spritecollide(player,enemies,False)
    if collisions:
        player.image.fill(BLACK)
        print("An Enemy ate you...")
        running=False

    safe=pygame.sprite.spritecollide(player,hbb,False)
    if safe:
        player.image.fill(GOOD_GREEN)
        player.image=pygame.Surface((5,5))
        pygame.time.delay(1000)
        for i in range(100):
            print("You Won!!")
        running=False

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()

