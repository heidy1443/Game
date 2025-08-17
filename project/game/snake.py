import pygame
import time
import random

def hungry_snack():
    pygame.init()
    screen=pygame.display.set_mode((600,600))
    pygame.display.set_caption("Hungry Snack!")
    clock=pygame.time.Clock()
    
    score=0
    square_pos=(300,300)
    square_size=9
    color=(random.randint(0,240),random.randint(0,240),random.randint(0,240))
    target_pos=(random.randint(50,550),random.randint(50,450))
    target_size=9
    
    running=True
    while running:
        screen.fill((0,0,0))
        snack=pygame.draw.rect(screen,color,square_pos,square_size)
        target=pygame.draw.rect(screen,(0,0,0),target_pos,target_size)
        
        font=pygame.font.Font(None,36)
        Time=time.time()
        score_text=font.render(f"Score:{score}|Time:{Time}",True,(255,255,255))
        screen.blit(score_text,(20,20))
        
        if snack.colliderect(target):
            