import pygame
import time
import random

def click_game():
    pygame.init()
    screen=pygame.display.set_mode((600,600))
    pygame.display.set_caption("click me!")
    clock=pygame.time.Clock()
    
    score=0
    circle_pos=(300,300)
    circle_radius=30
    start_time=time.time()
    game_duration=30
    color=(random.randint(0,240),random.randint(0,240),random.randint(0,240))
    
    running=True
    while running:
        screen.fill((255,255,255))
        pygame.draw.circle(screen,color,circle_pos,circle_radius)
        
        font=pygame.font.Font(None,36)
        elapsed=int(time.time()-start_time)
        remaining=max(0,game_duration-elapsed)
        score_text=font.render(f"Score:{score}|Time:{remaining}",True,(0,0,0))
        screen.blit(score_text,(20,20))
        
        if remaining<=0:
            running=False
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                distance=((mouse_pos[0]-circle_pos[0])**2+(mouse_pos[1]-circle_pos[1])**2)**0.5
                
                if distance<=circle_radius:
                    score+=1
                    circle_radius=random.randint(10,60)
                    circle_pos=random.randint(50,550),random.randint(50,450)
                    color=(random.randint(0,240),random.randint(0,240),random.randint(0,240))
                    
        
        pygame.display.flip()
        clock.tick(30)
        
    screen.fill((255,255,255))
    font=pygame.font.Font(None,50)
    text=font.render(f"Well done!Final Score:{score}",True,(0,0,0))
    screen.blit(text,(80,300))
    pygame.display.flip()
    pygame.time.wait(3000)
    
    pygame.quit()
    
    
click_game()    