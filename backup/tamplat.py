import pygame

pygame.init

screen=pygame.display.set_mode((1080,720)) 
pygame.display.set_caption("Coure N2 : jeux video")
clock=pygame.time.Clock()
runnig=True
while runnig:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            runnig=False
            
            
            
            
            
            
            
            clock.tick(60)
  # le rendu 
    pygame.display.flip()
    
    
    

pygame.quit