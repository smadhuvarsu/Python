import pygame
import time

pygame.init()

display_width = 1000
display_height = 700

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Find your Inner Rainbow!')

pygame.mixer.music.load('RM.mp3')
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
crashed = False

bg=pygame.image.load("Buddha_Bg.png")
RB=pygame.image.load("RB.png")
OB=pygame.image.load("OB.png")
YB=pygame.image.load("YB.png")
GB=pygame.image.load("GB.png")
BB=pygame.image.load("BB.png")
VB=pygame.image.load("VB.png")
PB=pygame.image.load("PB.png")


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.blit(bg, (0,0))
    pygame.display.update()
    time.sleep(3)

    gameDisplay.blit(RB, (0,0))
    pygame.display.update()
    time.sleep(3)

    gameDisplay.blit(OB, (0,0))
    pygame.display.update()
    time.sleep(3)

    gameDisplay.blit(YB, (0,0))
    pygame.display.update()
    time.sleep(3)

    gameDisplay.blit(GB, (0,0))
    pygame.display.update()
    time.sleep(3)

    gameDisplay.blit(BB, (0,0))
    pygame.display.update()
    time.sleep(3)

    gameDisplay.blit(VB, (0,0))
    pygame.display.update()
    time.sleep(3)

    gameDisplay.blit(PB, (0,0))
    pygame.display.update()
    time.sleep(3)
    
    clock.tick(60)

pygame.quit()
quit()
