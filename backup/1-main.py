import pygame
import random
pygame.init

screen = pygame.display.set_mode((700,500))

print(screen.get_rect())



clock = pygame.time.Clock()

# print(clock)
position_V=0
runing=True
couleurs=["white", "black","red","green","blue","yellow", "cyan","magenta","gray","orange","pink","purple","brown"]
while runing:
    # print(clock.get_fps())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
            
     
    
    surface = pygame.Surface((100,100))
    surface.fill("black") 
    
                                                                                                                                  
    screen.fill("gray" )    
    screen.blit(surface,(position_V,50))
    
    position_V+=2
    if position_V > 600:
        position_V=0
            
    clock.tick(60)
    
    pygame.display.flip()
    
    

pygame.quit()

